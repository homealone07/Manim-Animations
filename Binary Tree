from manim import *

class Main(Scene):
    def construct(self):
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText0 = MarkupText("""Explaining <span foreground=\"#fc6255\">Binary Trees</span>""", font_size=14, font="Consolas")
        IMarkupText0.move_to([0.0, 0.0, 0.0])
        IMarkupText0.scale(3.0)

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Create(IMarkupText0))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0 = Tree("t", parent=None)
        IText0 = INode0.label
        INode0.move_to([0.0, 0.0, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(ReplacementTransform(IMarkupText0, INode0))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0_target = INode0.copy()
        IText0_target = Text("5")
        IMarkupText1 = MarkupText("""A node can store a value.""", font_size=14, font="Consolas")
        INode0_target.move_to([0.09230769230769231, -0.9384615384615385, 0.0])
        IText0_target.move_to([0.09230769230769231, -0.9384615384615385, 0.0])
        IText0_target.match_color(INode0_target)
        IMarkupText1.move_to([0.07692307692307687, 1.3538461538461537, 0.0])
        IMarkupText1.scale(1.3)

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(IText0, IText0_target), Create(IMarkupText1))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
        self.remove(IMarkupText1)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0_target = INode0.copy()
        INode1 = Tree("2", parent=INode0)
        INode2 = Tree("7", parent=INode0)
        IText1 = INode1.label
        IText0_target = Text("5")
        IText2 = INode2.label
        IMarkupText2 = MarkupText("""Each node can hold up to <span foreground=\"#fc6255\">two</span> children.""", font_size=14, font="Consolas")
        INode0_target.move_to([0.09230769230769231, 0.3538461538461539, 0.0])
        INode1.move_to([-1.0923076923076922, -1.7846153846153845, 0.0])
        INode2.move_to([1.4, -1.8000000000000007, 0.0])
        IText1.move_to([-1.0923076923076922, -1.7846153846153845, 0.0])
        IText0_target.move_to([0.09230769230769231, 0.3538461538461539, 0.0])
        IText0_target.match_color(INode0_target)
        IText2.move_to([1.4, -1.8000000000000007, 0.0])
        IMarkupText2.move_to([-0.0769230769230771, 2.569230769230769, 0.0])
        IMarkupText2.scale(1.3)
        IParentEdge0 = ParentEdge(INode1)
        IParentEdge1 = ParentEdge(INode2)

       #PRINT TARGET ADD
        self.add(IParentEdge0)
        self.add(INode1)
        self.add(IParentEdge1)
        self.add(INode2)
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(IText0, IText0_target), Create(IMarkupText2))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
        self.remove(IMarkupText2)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0_target = INode0.copy()
        INode1_target = INode1.copy()
        INode2_target = INode2.copy()
        INode3 = Tree("1", parent=INode1)
        INode4 = Tree("4", parent=INode1)
        INode5 = Tree("8", parent=INode2)
        IMarkupText3 = MarkupText("""Recursively, they can build large data structures known as <big>binary trees</big>.""", font_size=14, font="Consolas")
        IText3 = INode3.label
        IText4 = INode4.label
        IText5 = INode5.label
        INode0_target.move_to([0.06153846153846154, 1.6153846153846145, 0.0])
        INode1_target.move_to([-3.5555555555555554, -0.25641025641025705, 0.0])
        INode2_target.move_to([3.5555555555555554, -0.25641025641025705, 0.0])
        INode3.move_to([-5.333333333333333, -2.1282051282051286, 0.0])
        INode4.move_to([-1.7777777777777777, -2.1282051282051286, 0.0])
        INode5.move_to([5.50940170940171, -2.1743589743589746, 0.0])
        IMarkupText3.move_to([-0.046153846153846434, 2.9692307692307693, 0.0])
        IMarkupText3.scale(1.2)
        IText3.move_to([-5.333333333333333, -2.1282051282051286, 0.0])
        IText4.move_to([-1.7777777777777777, -2.1282051282051286, 0.0])
        IText5.move_to([5.50940170940171, -2.1743589743589746, 0.0])
        IParentEdge2 = ParentEdge(INode3)
        IParentEdge3 = ParentEdge(INode4)
        IParentEdge4 = ParentEdge(INode5)

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode2, INode2_target), Transform(INode1, INode1_target), Transform(INode0, INode0_target), Create(IMarkupText3), FadeIn(INode3), FadeIn(IParentEdge2), FadeIn(INode4), FadeIn(IParentEdge3), FadeIn(INode5), FadeIn(IParentEdge4))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
        self.remove(IMarkupText3)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0_target = INode0.copy()
        INode1_target = INode1.copy()
        INode4_target = INode4.copy()
        INode3_target = INode3.copy()
        INode2_target = INode2.copy()
        INode5_target = INode5.copy()
        IMarkupText4 = MarkupText("""Now let&#x27;s take a look at <big>searching</big> through binary trees.""", font_size=14, font="Consolas")
        INode0_target.move_to([-3.046153846153846, 1.6461538461538452, 0.0])
        INode1_target.move_to([-4.524786324786324, -0.4410256410256417, 0.0])
        INode4_target.move_to([-3.7008547008547006, -2.6820512820512823, 0.0])
        INode3_target.move_to([-5.5948717948717945, -2.666666666666667, 0.0])
        INode2_target.move_to([-1.7059829059829061, -0.41025641025641135, 0.0])
        INode5_target.move_to([-0.7367521367521366, -2.666666666666667, 0.0])
        IMarkupText4.move_to([3.2, 0.12307692307692308, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode5, INode5_target), Transform(INode2, INode2_target), Transform(INode3, INode3_target), Transform(INode4, INode4_target), Transform(INode1, INode1_target), Transform(INode0, INode0_target), Create(IMarkupText4))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.2, 0.12307692307692308, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText9 = MarkupText("""Let&#x27;s go through the code.""", font_size=14, font="Consolas")
        IMarkupText9.move_to([2.030769230769231, 2.753846153846154, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Create(IMarkupText9))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
        self.remove(IMarkupText9)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = IMarkupText4.copy()
        IMathTex0 = MathTex(r"{}".format("val_{target} = 4"), font_size=50)
        IMathTex1 = MathTex(r"{}".format("val_{root} = 5"), font_size=50)
        IMarkupText4_target.move_to([3.1692307692307695, -0.30769230769230776, 0.0])
        IMathTex0.move_to([0.7999999999999998, 2.4923076923076923, 0.0])
        IMathTex0.set_color("#79df5f")
        IMathTex1.move_to([4.399999999999999, 2.446153846153846, 0.0])
        IMathTex1.set_color("#fc6255")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target), FadeIn(IMathTex1), FadeIn(IMathTex0))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(2.0)
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0_target = INode0.copy()
        IMathTex1_target = MathTex(r"{}".format("val_{curr} = 5"), font_size=50)
        INode0_target.set_color("#fce94f")
        IMathTex1_target.set_color("#fce94f")
        IMathTex1_target.move_to([4.399999999999999, 2.446153846153846, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(IMathTex1, IMathTex1_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  <span foreground=\"#bf4040\">if curr is None:</span>
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  <span foreground=\"#bf4040\">if curr.val &lt; val:</span>
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  <span foreground=\"#8ae234\">if curr.val &gt; val:</span>
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return <span foreground=\"#fce94f\">binarySearch(curr.left, val)</span>
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode1_target = INode1.copy()
        INode0_target = INode0.copy()
        IMathTex1_target = MathTex(r"{}".format("val_{curr} = 2"), font_size=50)
        INode1_target.set_color("#fce94f")
        INode0_target.set_color("#fc6255")
        IMathTex1_target.set_color("#fce94f")
        IMathTex1_target.move_to([4.399999999999999, 2.446153846153846, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(INode1, INode1_target), Transform(IMathTex1, IMathTex1_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
 <span foreground=\"#bf4040\"> if curr is None:</span>
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  <span foreground=\"#8ae234\">if curr.val &lt; val:</span>
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return <span foreground=\"#fce94f\">binarySearch(curr.right, val)</span>
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode4_target = INode4.copy()
        INode1_target = INode1.copy()
        IMathTex1_target = MathTex(r"{}".format("val_{curr} = 4"), font_size=50)
        INode4_target.set_color("#fce94f")
        INode1_target.set_color("#fc6255")
        IMathTex1_target.set_color("#fce94f")
        IMathTex1_target.move_to([4.399999999999999, 2.446153846153846, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode1, INode1_target), Transform(INode4, INode4_target), Transform(IMathTex1, IMathTex1_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  <span foreground=\"#bf4040\">if curr is None:</span>
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  <span foreground=\"#bf4040\">if curr.val &lt; val:</span>
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  <span foreground=\"#bf4040\">if curr.val &gt; val:</span>
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return <span foreground=\"#fce94f\">curr</span>""", font_size=14, font="Consolas")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText4, IMarkupText4_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode4_target = INode4.copy()
        IMarkupText4_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return <span foreground=\"#79df5f\">curr</span>""", font_size=14, font="Consolas")
        IMathTex1_target = MathTex(r"{}".format("val_{curr} = 4"), font_size=50)
        INode4_target.set_color("#79df5f")
        IMarkupText4_target.move_to([3.1692307692307695, -0.3076923076923077, 0.0])
        IMarkupText4_target.set_color("#eeeeec")
        IMathTex1_target.set_color("#79df5f")
        IMathTex1_target.move_to([4.399999999999999, 2.446153846153846, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode4, INode4_target), Transform(IMarkupText4, IMarkupText4_target), Transform(IMathTex1, IMathTex1_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
        self.remove(IMarkupText4)
        self.remove(IMathTex0)
        self.remove(IMathTex1)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode4_target = INode4.copy()
        IMarkupText5 = MarkupText("""How about searching for something that is <span foreground=\"#bf4040\">not</span> in the tree?""", font_size=14, font="Consolas")
        INode4_target.set_color("#fc6255")
        IMarkupText5.move_to([3.153846153846154, -0.2, -1.5407439555097887e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode4, INode4_target), Create(IMarkupText5))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMathTex2 = MathTex(r"{}".format("val_{target} = 6"), font_size=50)
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -2.311115933264683e-33])
        IMathTex2.move_to([1.5230769230769232, 2.261538461538462, 0.0])
        IMathTex2.set_color("#79df5f")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target), FadeIn(IMathTex2))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMathTex2_target = IMathTex2.copy()
        IMathTex2_target.set_color("#bf4040")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMathTex2, IMathTex2_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMathTex2_target = IMathTex2.copy()
        IMathTex2_target.set_color("#79df5f")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMathTex2, IMathTex2_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMathTex3 = MathTex(r"{}".format("val_{root} = 5"), font_size=50)
        IMathTex3.move_to([4.6000000000000005, 2.3076923076923075, 0.0])
        IMathTex3.set_color("#fc6255")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(FadeIn(IMathTex3))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0_target = INode0.copy()
        IMathTex3_target = MathTex(r"{}".format("val_{curr} = 5"), font_size=50)
        INode0_target.set_color("#fce94f")
        IMathTex3_target.set_color("#fce94f")
        IMathTex3_target.move_to([4.6000000000000005, 2.3076923076923075, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(IMathTex3, IMathTex3_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  <span foreground=\"#bf4040\">if curr is None:</span>
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  <span foreground=\"#79df5f\">if curr.val &lt; val:</span>
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return <span foreground=\"#fce94f\">binarySearch(curr.right, val)</span>
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode2_target = INode2.copy()
        INode0_target = INode0.copy()
        IMathTex3_target = MathTex(r"{}".format("val_{curr} = 7"), font_size=50)
        INode2_target.set_color("#fce94f")
        INode0_target.set_color("#fc6255")
        IMathTex3_target.set_color("#fce94f")
        IMathTex3_target.move_to([4.6000000000000005, 2.3076923076923075, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(INode2, INode2_target), Transform(IMathTex3, IMathTex3_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
 <span foreground=\"#bf4040\"> if curr is None:</span>
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
 <span foreground=\"#bf4040\"> if curr.val &lt; val:</span>
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  <span foreground=\"#8ae234\">if curr.val &gt; val:</span>
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return <span foreground=\"#fce94f\">binarySearch(curr.left, val)</span>
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode2_target = INode2.copy()
        IMathTex3_target = MathTex(r"{}".format("val_{curr} = N/A"), font_size=50)
        INode2_target.set_color("#fc6255")
        IMathTex3_target.set_color("#fce94f")
        IMathTex3_target.move_to([4.953846153846154, 2.2307692307692304, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode2, INode2_target), Transform(IMathTex3, IMathTex3_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  <span foreground=\"#8ae234\">if curr is None:</span>
    return None
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return <span foreground=\"#fce94f\">None</span>
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText5_target = MarkupText("""def binarySearch(curr, val):
  if curr is None:
    return <span foreground=\"#bf4040\">None</span>
      
  if curr.val &lt; val:
    return binarySearch(curr.right, val)
      
  if curr.val &gt; val:
    return binarySearch(curr.left, val)
  
  return curr""", font_size=14, font="Consolas")
        IMathTex3_target = IMathTex3.copy()
        IMarkupText5_target.move_to([3.153846153846154, -0.19999999999999996, -3.0814879110195774e-33])
        IMathTex3_target.set_color("#bf4040")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText5, IMarkupText5_target), Transform(IMathTex3, IMathTex3_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(2.0)
       #PRINT REMOVED
        self.remove(IMarkupText5)
        self.remove(IMathTex3)
        self.remove(IMathTex2)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode2_target = INode2.copy()
        INode5_target = INode5.copy()
        INode4_target = INode4.copy()
        INode1_target = INode1.copy()
        INode3_target = INode3.copy()
        INode0_target = INode0.copy()
        INode2_target.move_to([4.54017094017094, -0.3333333333333344, 0.0])
        INode5_target.move_to([5.50940170940171, -2.5897435897435903, 0.0])
        INode4_target.move_to([2.545299145299145, -2.6051282051282056, 0.0])
        INode1_target.move_to([1.7213675213675224, -0.36410256410256475, 0.0])
        INode3_target.move_to([0.6512820512820485, -2.5897435897435903, 0.0])
        INode0_target.move_to([3.199999999999999, 1.7230769230769218, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(INode3, INode3_target), Transform(INode1, INode1_target), Transform(INode4, INode4_target), Transform(INode5, INode5_target), Transform(INode2, INode2_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7 = MarkupText("""Now, let&#x27;s look at how we <big>insert</big> a node into the tree.""", font_size=14, font="Consolas")
        IMarkupText7.move_to([-3.615384615384616, -0.15384615384615385, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Create(IMarkupText7))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""Now, let&#x27;s look at how we <big>insert</big> a node into the tree.""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.615384615384616, -0.15384615384615385, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    if curr.right is None:
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.615384615384616, -0.15384615384615397, -7.703719777548943e-34])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = IMarkupText7.copy()
        IMathTex4 = MathTex(r"{}".format("val_{node} = 6"), font_size=50)
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])
        IMathTex4.move_to([-5.0307692307692315, 2.138461538461539, 0.0])
        IMathTex4.set_color("#fc6255")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target), FadeIn(IMathTex4))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode0_target = INode0.copy()
        IMathTex5 = MathTex(r"{}".format("val_{curr} = 5"), font_size=50)
        INode0_target.set_color("#fce94f")
        IMathTex5.move_to([-1.476923076923077, 2.123076923076923, 0.0])
        IMathTex5.set_color("#fce94f")

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), FadeIn(IMathTex5))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  <span foreground=\"#79df5f\">if curr.val &lt; node.val:</span>
    if curr.right is None:
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    <span foreground=\"#bf4040\">if curr.right is None:</span>
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    if curr.right is None:
      curr.right = node
    <span foreground=\"#79df5f\">else:</span>
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    if curr.right is None:
      curr.right = node
    else:
      <span foreground=\"#fce94f\">treeInsert(curr.right, node)</span>
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode2_target = INode2.copy()
        INode0_target = INode0.copy()
        IMathTex5_target = MathTex(r"{}".format("val_{curr} = 7"), font_size=50)
        INode2_target.set_color("#fce94f")
        INode0_target.set_color("#fc6255")
        IMathTex5_target.set_color("#fce94f")
        IMathTex5_target.move_to([-1.476923076923077, 2.123076923076923, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode0, INode0_target), Transform(INode2, INode2_target), Transform(IMathTex5, IMathTex5_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    if curr.right is None:
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
 <span foreground=\"#bf4040\"> if curr.val &lt; node.val:</span>
    if curr.right is None:
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    if curr.right is None:
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  <span foreground=\"#79df5f\">elif curr.val &gt; node.val:</span>
    if curr.left is None:
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    if curr.right is None:
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    <span foreground=\"#79df5f\">if curr.left is None:</span>
      curr.left = node
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText7_target = MarkupText("""def treeInsert(curr, node):
  if curr.val &lt; node.val:
    if curr.right is None:
      curr.right = node
    else:
      treeInsert(curr.right, node)
      
  elif curr.val &gt; node.val:
    if curr.left is None:
      <span foreground=\"#79df5f\">curr.left = node</span>
    else:
      treeInsert(curr.left, node)""", font_size=14, font="Consolas")
        IMarkupText7_target.move_to([-3.661538461538462, -0.7230769230769232, 0.0])

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText7, IMarkupText7_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode6 = Tree("6", parent=INode2)
        INode4_target = INode4.copy()
        IText6 = INode6.label
        INode6.move_to([3.8461538461538463, -2.6307692307692307, 0.0])
        INode6.set_parent(INode2)
        INode4_target.move_to([2.3145299145299143, -2.620512820512821, 0.0])
        IText6.move_to([3.8461538461538463, -2.6307692307692307, 0.0])
        IParentEdge5 = ParentEdge(INode6)

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode4, INode4_target), FadeIn(INode6), FadeIn(IParentEdge5))
       #PRINT REMOVED
        self.remove(IMathTex5)
        self.remove(IMathTex4)
        self.remove(IMarkupText7)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        INode2_target = INode2.copy()
        INode0_target = INode0.copy()
        INode1_target = INode1.copy()
        INode3_target = INode3.copy()
        INode4_target = INode4.copy()
        INode5_target = INode5.copy()
        INode6_target = INode6.copy()
        IMarkupText8 = MarkupText("""Binary Trees""", font_size=14, font="Consolas")
        INode2_target.set_color("#fc6255")
        INode2_target.move_to([3.5555555555555554, -0.3487179487179495, 0.0])
        INode0_target.move_to([-0.09230769230769387, 1.3999999999999988, 0.0])
        INode1_target.move_to([-3.5555555555555554, -0.3487179487179495, 0.0])
        INode3_target.move_to([-5.333333333333332, -2.1743589743589746, 0.0])
        INode4_target.move_to([-1.7777777777777777, -2.1743589743589746, 0.0])
        INode5_target.move_to([5.494017094017095, -2.3282051282051284, 0.0])
        INode6_target.move_to([1.4923076923076923, -2.2615384615384615, 0.0])
        IMarkupText8.move_to([-0.2153846153846154, 2.907692307692308, 0.0])
        IMarkupText8.scale(2.0)

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(INode6, INode6_target), Transform(INode5, INode5_target), Transform(INode4, INode4_target), Transform(INode3, INode3_target), Transform(INode1, INode1_target), Transform(INode0, INode0_target), Transform(INode2, INode2_target), FadeIn(IMarkupText8))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(1.0)
       #PRINT REMOVED
        self.remove(INode5)
        self.remove(IParentEdge4)
        self.remove(INode6)
        self.remove(IParentEdge5)
        self.remove(INode2)
        self.remove(IParentEdge1)
        self.remove(INode4)
        self.remove(IParentEdge3)
        self.remove(INode3)
        self.remove(IParentEdge2)
        self.remove(INode1)
        self.remove(IParentEdge0)
        self.remove(INode0)

       #PRINT MOBJ FUNCS
       #PRINT TARGETS
        IMarkupText8_target = MarkupText("""<u>Binary Trees</u>""", font_size=14, font="Consolas")
        IMarkupText8_target.move_to([0.04615384615384599, 1.1102230246251565e-16, 0.0])
        IMarkupText8_target.scale(4.0)

       #PRINT TARGET ADD
       #PRINT ANIMS
        self.play(Transform(IMarkupText8, IMarkupText8_target))
       #PRINT REMOVED
       #PRINT MOBJ FUNCS
       #PRINT TARGETS
       #PRINT TARGET ADD
       #PRINT ANIMS
        self.wait(2.0)

class Tree(VGroup):
    def __init__(self, text="t", parent=None):
        super().__init__()
        self.label = Text(text)
        self.container = Circle(radius=0.6)
        self.add(self.label, self.container)
        self.set_color(RED)
        self.parent = parent

    def change_text_transform(self, text):
        target = Text(text)
        target.match_color(self.label)
        target.move_to(self.label.get_center())

        return Transform(self.label, target)
        
    def set_parent(self, parent):
        self.parent = parent

class ParentEdge(Line):
    def __init__(self, node):
        self.node = node
        super().__init__(
            node.get_bottom() if node.parent is None else node.parent.get_bottom(),
            node.get_top(),
            color=RED,
        )
        self.add_updater(lambda mob: self.update_line(mob))

    def update_line(self, line):
        if self.node.parent is None:
            return 

        line.put_start_and_end_on(self.node.parent.get_bottom(), self.node.get_top())


