dashed=[]
count=8
for ang in range(count):
  angle=PI*2/count*ang
  line=DashedLine(start=np.array([math.cos(angle),math.sin(angle),0]),end=np.array([math.cos(angle)*2,math.sin(angle)*2,0]),color=YELLOW)
  line.add_updater(lambda mob,dt:mob.rotate(DEGREES,about_point=ORIGIN))
  dashed.append(line)

dash=VGroup(*dashed)
self.play(FadeIn(dash,run_time=.5))
