from manim import *

#prepare animations for the arrows
def get_anim(Grid, angle, WHITE=True):
	anim_group = []
	for i in range(len(Grid)):
		for j in range(len(Grid[0])):
			anim_group.append(Rotate(
				Grid[i][j], angle=angle, about_point=Grid[i][j].get_center()
				)
			)
	return anim_group 

#Change the group accordingly after each iteration
def prepare_group(Grid, angle):
	for i in range(len(Grid)):
		for j in range(len(Grid[0])):
			Grid[i][j].rotate(angle)
	return Grid

class Illusion(Scene):
	def construct(self):
		a = 1 #side length of square

		Right_isoceles = Polygram([[-a,0,0],
					   [0,a,0],
					   [a,0,0]], stroke_width=0, )

		Rectangle = Polygram(
		    [
			[-a/2,0.01,0],
			[a/2,0.01,0],  #the 0.01 for floating point madness
			[a/2,-a,0],
			[-a/2,-a,0]
		    ], 
		    stroke_width=0, 
		    
		)

		base_white = VGroup(Right_isoceles, Rectangle).set_fill(WHITE, 1)
		base_black = base_white.copy().set_fill(BLACK, 1)
		base_white.shift(config["frame_width"]/2*LEFT + config["frame_height"]/2*DOWN)
		base_black.shift(
		(config["frame_width"]/2 - base_black.width/2)*LEFT + (config["frame_height"]/2 - base_black.height/2)*DOWN
		)

		a_row_white = VGroup(
		    *[
			base_white.copy().shift(base_white.width*n*RIGHT) 
				      for n in range(int(config["frame_width"]/base_white.width)+2)
		    ]
		)
		
		a_row_black = VGroup(
		    *[
			base_black.copy().shift(base_black.width*n*RIGHT) 
				      for n in range(int(config["frame_width"]/base_black.width)+2)
		    ]
		)

		Grid_white = VGroup(
		    *[
			a_row_white.copy().shift(UP*i*base_white.height)
			if i%2==0 else a_row_white.copy().shift(UP*i*base_white.height + LEFT*base_white.width)
			
				for i in range(int(config["frame_height"]/base_white.height)+1)
		    ]
		)

		Grid_black = VGroup(
		    *[
			a_row_black.copy().shift(UP*i*base_black.height)
			if i%2==0 else a_row_black.copy().shift(UP*i*base_black.height + LEFT*base_black.width)
			
				for i in range(int(config["frame_height"]/base_black.height)+1)
		    ]
		)

		prepare_group(Grid_black, -PI) #because I haven't constructed the grid properly
		
		for _ in range(4):
			self.play(AnimationGroup(*get_anim(Grid_white, PI/2)), lag_ratio=0.00)
			self.add(prepare_group(Grid_black, PI/2))
			self.camera.background_color=WHITE
			self.play(AnimationGroup(*get_anim(Grid_black, PI/2)), lag_ratio=0.00)
			self.camera.background_color=BLACK
			self.add(prepare_group(Grid_white, PI/2))
