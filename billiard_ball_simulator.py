from vpython import *
import Table
from time import sleep
from BilliardBall import ball_radius, BilliardBall, collision1, m, incidence_angle

# initialization
g = 386  # 9.8*100/2.54 inch
t = 0
dt = 0.001

gd = graph(width=600, height=150, xmin=0, ymin=0)
Ek = gcurve(graph=gd, color=color.cyan)

balls = []
v_log = []
new_v_log = []
for i in range(16):
	contact = True
	temp_ball = BilliardBall(i)
	temp_pos = vec(0, 0, 0)
	while contact:
		contact = False
		temp_pos = vec((random() - 0.5) * (Table.p_length - ball_radius), ball_radius,
		               (random() - 0.5) * (Table.p_width - ball_radius))
		for j in range(len(balls)):
			if mag(temp_pos - balls[j].pos) <= ball_radius * 2:
				contact = True
	temp_ball.pos = temp_ball.name.pos = temp_pos
	v_log.append(temp_ball.v)
	new_v_log.append(temp_ball.v)
	balls.append(temp_ball)

f_coe = 0.015
target = 1  # the ball cue ball targets
theta = 0  # angle of incidence
cue_ball_v0 = vec(0, 0, 0)
# cue_ball_v0 = vec(20 * random() + 10, 0, 20 * random() + 10)  # use this line to randomize cue ball velocity

# initialization end

# use this line to randomize cue ball position
# cue_ball_pos0 = vec((random() - 0.5) * (Table.p_length - ball_radius),
#                     ball_radius,
#                     (random() - 0.5) * (Table.p_width - ball_radius))
# balls[0].pos = cue_ball_pos0


def set_shot():
	global target, theta, cue_ball_v0, f_coe
	# f_coe = float(input('enter friction coefficient: '))
	target = int(input('target ball (1~15): '))  # the ball cue ball targets
	theta = float(input('angle of incidence (counter-clockwise, -90 ~ 90 degrees): ')) * pi / 180
	# only change the number, not the vector!!
	cue_ball_v0 = float(input('v0: ')) *\
	              norm((balls[target].pos - balls[0].pos).
	                   rotate(angle=incidence_angle(theta, balls[0], balls[target]), axis=vector(0, 1, 0)))
	sleep(3)


def run():
	global t
	balls[0].v = cue_ball_v0
	v_log[0] = cue_ball_v0
	while True:
		rate(1 / dt)
		for i in range(16):
			update = False
			for j in range(16):
				if i != j and balls[j].visible and balls[i].visible:
					if mag(balls[i].pos - balls[j].pos) <= ball_radius * 2 \
							and dot(balls[i].pos - balls[j].pos, balls[i].v - balls[j].v) <= 0:
						temp1, temp2 = collision1(balls[i], balls[j])
						update = True
						new_v_log[i] += temp1

			wall_factor = balls[i].wall_collision()
			if update:
				new_v_log[i].x *= wall_factor.x
				new_v_log[i].z *= wall_factor.z
			else:
				new_v_log[i].x = v_log[i].x * wall_factor.x
				new_v_log[i].z = v_log[i].z * wall_factor.z

		total_Ek = 0
		for i in range(16):
			# check if the ball goes in hole; if so, make it invisible and v = 0
			for j in range(len(Table.holes)):
				if sqrt((balls[i].pos.x - Table.holes[j].pos.x) ** 2 + (balls[i].pos.z - Table.holes[j].pos.z) ** 2) \
						<= Table.holes[j].size.y / 2:
					balls[i].visible = False
					balls[i].name.visible = False
					balls[i].v = vec(0, 0, 0)

			if balls[i].visible:
				balls[i].pos += balls[i].v * dt
				balls[i].name.pos = balls[i].pos
				balls[i].v = new_v_log[i] - g * f_coe * norm(new_v_log[i]) * dt

			balls[i].Ek = (m * mag2(balls[i].v)) / 2
			total_Ek += balls[i].Ek
			v_log[i] = balls[i].v
			new_v_log[i] = vec(0, 0, 0)

		Ek.plot(t, total_Ek)
		if total_Ek < 1e-5 or not balls[0].visible:  # terminate game when cue ball is gone
			break
		t += dt


# main loop
while True:
	set_shot()
	print('start')
	run()
	print('done!')
	if not balls[0].visible:
		print('Game over, you lose!')
		break
