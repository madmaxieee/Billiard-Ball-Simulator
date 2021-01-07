from vpython import *
from Table import p_length, p_width

e = 0.98 # coefficient of restitution

ball_radius = 2.25 / 2  # ball radius
m = 0.17  # unit: kg

# colors of balls according to their numbers
ball_colors = [color.black, color.yellow, color.blue, color.red,
               color.purple, color.orange, color.green, vec(0.6, 0.3, 0.2)]
for i in range(1, 8):
	ball_colors[i] -= vec(0.2, 0.2, 0.2)


def collision1(ball1, ball2):
	v1x = (ball1.pos - ball2.pos) * dot(ball1.v , ball1.pos - ball2.pos) / mag(ball1.pos - ball2.pos) ** 2
	v2x = (ball2.pos - ball1.pos) * dot(ball2.v , ball2.pos - ball1.pos) / mag(ball2.pos - ball1.pos) ** 2
	# v1prime = ball1.v - 2 * m / (m + m) * (ball1.pos - ball2.pos) * \
	#           dot(ball1.v - ball2.v, ball1.pos - ball2.pos) / mag(ball1.pos - ball2.pos) ** 2
	v1prime = ball1.v - v1x + ((1+e)*(m*v1x+m*v2x)/(m+m)-e*v1x)
	# v2prime = ball2.v - 2 * m / (m + m) * (ball2.pos - ball1.pos) * \
	#           dot(ball2.v - ball1.v, ball2.pos - ball1.pos) / mag(ball2.pos - ball1.pos) ** 2
	v2prime = ball2.v - v2x + ((1 + e) * (m * v2x + m * v1x) / (m + m) - e * v2x)

	#return sqrt(1 - energy_loss1) * v1prime, sqrt(1 - energy_loss1) * v2prime
	return v1prime,v2prime


class BilliardBall(sphere):

	def __init__(self, num):
		sphere.__init__(self)
		self.radius = ball_radius
		self.pos = vec(0, 0, 0)
		self.v = vec(0, 0, 0)
		self.Ek = 0
		self.name = label(pos=self.pos, text=str(num), xoffset=5, yoffset=5)
		if num > 0:
			self.color = ball_colors[num % 8]
		else:
			self.color = vec(0.7, 0.7, 0.7)

	def wall_collision(self):
		temp = vec(1, 1, 1)
		if (self.pos.x + ball_radius >= p_length / 2 and self.v.x > 0) \
				or (self.pos.x - ball_radius <= -p_length / 2 and self.v.x < 0):
			# temp.x *= -sqrt(1 - energy_loss2)
			temp.x *= -e

		if (self.pos.z + ball_radius >= p_width / 2 and self.v.z > 0) \
				or (self.pos.z - ball_radius <= -p_width / 2 and self.v.z < 0):
			# temp.z *= -sqrt(1 - energy_loss2)
			temp.z *= -e
		return temp


def incidence_angle(theta, ball1, ball2):
	if theta == 0:
		return 0
	d = mag(ball1.pos - ball2.pos)
	temp = (d - 2 * ball_radius * cos(theta)) / sqrt(d ** 2 + 4 * ball_radius ** 2 - 4 * d * ball_radius * cos(theta))
	return  theta / abs(theta) * acos(temp)
