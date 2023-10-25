from manim import *
import manim
import time
import random
import numpy as np
# manim.config.save_last_frame = True

class RectangleExample(Scene):
    def construct(self):
        #Rectangle cration
        main_brownie = Rectangle(width=6.0, height=3.0, color=DARK_BROWN, fill_opacity=1)
        self.play(DrawBorderThenFill(main_brownie))
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI/2).scale(1.78)
        self.play(FadeIn(main_brownie))
        # self.wait(5 )
        # main_brownie = Rectangle(width=0.8, height=-1.08, color=BLACK,fill_opacity=1).rotate(-0.8 * PI).move_to([-0.77, 0.5, 0])
        # self.play(Create(main_brownie))
        # self.wait(15)
        # self.play(Uncreate(main_brownie))
        for i in range(6):
            self.wait(0.1)
            main_brownie = Rectangle(width=1.2*np.random.randn(), height=0.60*np.random.randn(), color=BLACK, fill_opacity=1).rotate(2*PI*np.random.randn()).move_to([np.random.randn(), np.random.randn(), 0])
            self.play(Create(main_brownie))
            self.play(FadeOut(main_brownie))


class Hint1_P1(Scene):
    def construct(self):
        rules = Text('Hint 1:')
        self.play(Write(rules))
        self.play(rules.animate.shift([-5, 3, 0]))
        #Rectangle cration
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI/2).scale(1.78)
        self.play(FadeIn(main_brownie))
        self.wait(7)
        self.play(Create(Line([3, 1.5, 0],[-3, -1.5, 0])))
        self.play(Create(Line([3, 0, 0], [-3, 0, 0])))
        self.play(Create(Line([0, 1.5, 0], [0, -1.5, 0])))
        self.play(Create(Line([3, -1.5, 0], [-3, 1.5, 0])))

        #Rotator 1
        sp=[3.02,0,0]
        ep=[-3.02,0,0]
        step=0.06
        l=Line(sp, ep)
        self.add(l)
        for i in range(int(1.5/step)-1):
            sp[1] += step
            ep[1] -= step
            l.put_start_and_end_on([sp[0], sp[1]+step, sp[2]], [ep[0], ep[1]-step, ep[2]])
            self.wait(0.1)
        self.remove(l)
        # # Rotator 2
        sp = [3.02, 1.5, 0]
        ep = [-3.02, -1.5, 0]
        l = Line(sp, ep)
        self.add(l)
        for i in range(int(6 / step) - 1):
            sp[0] -= step
            ep[0] += step
            l.put_start_and_end_on([sp[0]-step, sp[1], sp[2]], [ep[0]+step, ep[1], ep[2]])
            self.wait(0.1)
        self.remove(l)
        sp = [3.02, -1.5, 0]
        ep = [-3.02, 1.5, 0]
        l = Line(sp, ep)
        self.add(l)
        for i in range(int(1.5/step)-1):
            sp[1] += step
            ep[1] -= step
            l.put_start_and_end_on([sp[0], sp[1]+step, sp[2]], [ep[0], ep[1]-step, ep[2]])
            self.wait(0.1)
        self.remove(l)

class Hint1_P2(Scene):
    def construct(self):
        #Rectangle cration
        main_brownie = Rectangle(width=6.0, height=3.0, color=LIGHT_BROWN, fill_opacity=1)
        self.add(main_brownie)
        main_brownie = Rectangle(width=1.0 , height=0.5, color=BLACK,fill_opacity=1)
        self.add(main_brownie)
        self.add(Line([3, 1.5, 0],[-3, -1.5, 0]))
        self.add(Line([3, 0, 0], [-3, 0, 0]))
        self.add(Line([0, 1.5, 0], [0, -1.5, 0]))
        self.add(Line([3, -1.5, 0], [-3, 1.5, 0]))
        self.add(Circle(radius=0.1, color=MAROON_E, fill_opacity=1))
        self.wait(5)
        main_brownie = Rectangle(width=6.0, height=3.0, color=LIGHT_BROWN, fill_opacity=1)
        self.add(main_brownie)
        self.add(Circle(radius=0.1, color=MAROON_E, fill_opacity=1))
        self.wait(5)
        main_brownie = Rectangle(width=1.0 , height=0.5, color=BLACK,fill_opacity=1)
        self.add(main_brownie)
        self.add(Circle(radius=0.1, color=MAROON_E, fill_opacity=1))
        self.wait(5)

class Hint2(Scene):
    def construct(self):
        rules = Text('Hint 3:')
        self.play(Write(rules))
        self.play(rules.animate.shift([-5, 3, 0]))
        # Rectangle creation
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI / 2).scale(1.78)
        brownie_target = ImageMobject("media/images/Main/Brownie.png").scale(1.78).move_to([-2, 0, 0])
        self.play(FadeIn(main_brownie))
        main_brownie = Rectangle(width=0.8, height=-1.08, color=BLACK,fill_opacity=1).rotate(-0.8 * PI).move_to([-0.77, 0.5, 0])
        self.play(Create(main_brownie))
        self.wait(5)
        #Rotator small
        sp = [-0.1, 0.3, 0]
        ep = [-1.44, 0.72, 0]
        step = 0.02
        r=1.32
        l = Line(sp, ep)
        self.play(Create(l))
        for i in range(int(0.52/step)-1):
            self.wait(0.07)
            sp[1] -= step
            sp[0] -= r*step
            ep[0] += r*step
            ep[1] += step
            l.put_start_and_end_on([sp[0], sp[1], sp[2]], [ep[0], ep[1], ep[2]])
        for i in range(int(0.73/step)-1):
            self.wait(0.07)
            sp[1] += r*step
            sp[0] -= step
            ep[0] += step
            ep[1] -= r*step
            l.put_start_and_end_on([sp[0], sp[1], sp[2]], [ep[0], ep[1], ep[2]])
        self.wait(0.7)
        #Rotator Large
        sp = [3.02, 1.5, 0]
        ep = [-3.02, -1.5, 0]
        step=0.1
        l = Line(sp, ep)
        self.play(Create(l))
        for i in range(int(6 / step) - 1):
            sp[0] -= step
            ep[0] += step
            l.put_start_and_end_on([sp[0] - step, sp[1], sp[2]], [ep[0] + step, ep[1], ep[2]])
            self.wait(0.07)
        self.remove(l)
        sp = [3.02, -1.5, 0]
        ep = [-3.02, 1.5, 0]
        l = Line(sp, ep)
        self.add(l)
        for i in range(int(3/ step) - 1):
            sp[1] += step
            ep[1] -= step
            l.put_start_and_end_on([sp[0], sp[1] + step, sp[2]], [ep[0], ep[1] - step, ep[2]])
            self.wait(0.07)
        self.wait(9)


class Sol(Scene):
    def construct(self):
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI / 2).scale(1.78)
        self.add(main_brownie)
        femboy = ImageMobject("media/images/Main/femboy.png").move_to([5, -1, 0]).scale(0.8)
        self.add(femboy)
        self.add(Text("How to cut in half ?").move_to([0, 2.5, 0]).scale(1.2))
        main_brownie = Rectangle(width=0.8, height=-1.08, color=BLACK,fill_opacity=1).rotate(-0.8 * PI).move_to([-0.77, 0.5, 0])
        self.play(Create(main_brownie))
        # self.add(Circle(radius=0.1, color=MAROON_E, fill_opacity=1).move_to([-0.77, 0.5, 0]))
        #Rotator small
        sp = [-0.1, 0.3, 0]
        ep = [-1.44, 0.72, 0]
        step = 0.00125
        r=1.32
        l = Line(sp, ep)
        self.add(l)
        ostep=0.05
        osp = [3.02, 1.5, 0]
        oep = [-3.02, -1.5, 0]
        ol = Line(osp, oep)
        self.add(ol)
        for i in range(104):
            self.wait(0.04)
            sp[1] -= step
            sp[0] -= r*step
            ep[0] += r*step
            ep[1] += step
            l.put_start_and_end_on([sp[0], sp[1], sp[2]], [ep[0], ep[1], ep[2]])
            osp[0] -= ostep
            oep[0] += ostep
            ol.put_start_and_end_on([osp[0] - ostep, osp[1], osp[2]], [oep[0] + ostep, oep[1], oep[2]])
        self.wait(5)





class Sol2(Scene):
    def construct(self):
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI / 2).scale(1.78)
        self.add(main_brownie)
        femboy = ImageMobject("media/images/Main/femboy.png").move_to([5, -1, 0]).scale(0.8)
        self.add(femboy)
        main_brownie = Rectangle(width=0.8, height=-1.08, color=BLACK,fill_opacity=1).rotate(-0.8 * PI).move_to([-0.77, 0.5, 0])
        self.add(main_brownie)
        self.add(Circle(radius=0.06, color=BLUE, fill_opacity=1).move_to([-0.77, 0.5, 0]))
        self.add(Circle(radius=0.06, color=BLUE, fill_opacity=1))
        l=Line([-0.77, 0.5, 0],[0,0,0])
        m=-0.77/0.5
        l2 = Line([m*0.48, 0.48, 0], [m*1.52, 1.52, 0])
        l3 = Line([m*0.48, 0.48, 0], [m*-1.52, -1.52, 0])
        self.play(Create(l))
        self.wait(2)
        self.play(Create(l2), Create(l3))
        self.wait(5)




class Title(Scene):
    def construct(self):
        #Rectangle cration

        main_brownie = Text("Prolverr").scale(1.3).move_to(UP/3)
        sub = Text("The femboy brownie problem").scale(0.5).move_to(DOWN/2)
        femboy = ImageMobject("media/images/Main/femboy.png").move_to([2,-8,0])
        self.play(Write(main_brownie))
        self.wait(.4)
        self.play(FadeIn(sub))
        self.wait(1.7)
        self.add(femboy)
        self.play(femboy.animate.shift(UP*7))
        self.play(femboy.animate.shift(DOWN * 0.25), run_time=0.7)
        self.wait(10)

class Rules(Scene):
    def construct(self):
        rules = Text('Rules:')
        self.play(Write(rules))
        self.play(rules.animate.shift([-5, 3, 0]))

        rule1 = Text('1. Brownie is a rectangle').move_to([-1, 2, 0])
        rule2 = Text('2. A smaller rectangle within the brownie is missing, at a random location, size and angle').move_to([-1, 1, 0])
        rule3 = Text('3. Using 1 straight cut find a method to cut the brownie in exactly half \nfor every location, size and angle of the missing piece').move_to([-1, 0, 0])
        x = VGroup(rule1, rule2, rule3).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.5)
        self.play(DrawBorderThenFill(x).set_run_time(2.5))
        self.play(Write(Text("Good Luck!").scale(2.5).move_to(DOWN*2.5)))
        question = Text("Over all possible configurations what is the longest amount of time \nyou would need to wait to guarantee that the table has no more ants?", should_center=True).scale(0.5).move_to([0,0.5,0])
        # self.play(Write(question).set_run_time(6))
        # self.wait(1)
        # or_text = Text("or").scale(0.5).move_to([0,-0.5,0])
        # self.play(FadeIn(or_text))
        # self.wait(1)
        # new_question = Text("What is the longest time the ants would take to walk off the table?").scale(0.5).move_to([0,-1,0])
        # self.play(Write(new_question).set_run_time(3))
        self.wait(10)

class Hint2_readjust(Scene):
    def construct(self):
        rules = Text('Hint 2:')
        self.play(Write(rules))
        self.play(rules.animate.shift([-5, 3, 0]))
        #Rectangle creation
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI/2).scale(1.78)
        brownie_target = ImageMobject("media/images/Main/Brownie.png").scale(1.78).move_to([-2, 0, 0])
        self.play(FadeIn(main_brownie))
        empty = Rectangle(width=0.8, height=-1.08, color=BLACK,fill_opacity=1).rotate(-0.8 * PI).move_to([-0.77, 0.5, 0])
        self.play(Create(empty))
        empty_target= Rectangle(width=3, height=4, color=BLACK,fill_opacity=1).move_to([2, 0, 0])
        empty_target_border = Rectangle(width=3.05, height=4.05, color=WHITE, fill_opacity=1).rotate(PI).move_to([2, 0, 0])
        self.wait(6)
        self.play(Transform(empty,empty_target))
        self.add(empty_target_border, empty_target)
        self.play(Transform(main_brownie,brownie_target))
        self.wait(3)
        self.play(Create(DashedLine([2,2,0],[2,-2,0], color=WHITE, stroke_width=5)), Create(DashedLine([-2,3,0],[-2,-3,0], color=WHITE)))
        self.wait(10)



class SolRe(Scene):
    def construct(self):
        rules = Text('Solution').scale(2)
        target_rules=Text('Solution').scale(1).move_to([-5, 3, 0])
        self.play(Write(rules))
        self.play(Transform(rules,target_rules))
        #Rectangle cration
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI/2).scale(1.78)
        self.play(FadeIn(main_brownie))
        self.wait(1)
        femboy = ImageMobject("media/images/Main/femboy.png").move_to([5, -8, 0]).scale(0.8)
        self.add(femboy)
        self.play(femboy.animate.shift(UP*7), run_time=3)
        self.wait(2)
        # self.play(femboy.animate.shift(DOWN * 0.25), run_time=0.7)
        #Rotator 1
        sp=[3.02,0,0]
        ep=[-3.02,0,0]
        step=0.06
        l=Line(sp, ep)
        self.add(l)
        for i in range(int(1.5/step)-1):
            sp[1] += step
            ep[1] -= step
            l.put_start_and_end_on([sp[0], sp[1]+step, sp[2]], [ep[0], ep[1]-step, ep[2]])
            self.wait(0.1)
        self.remove(l)
        # # Rotator 2
        sp = [3.02, 1.5, 0]
        ep = [-3.02, -1.5, 0]
        l = Line(sp, ep)
        self.add(l)
        for i in range(int(6 / step) - 1):
            sp[0] -= step
            ep[0] += step
            l.put_start_and_end_on([sp[0]-step, sp[1], sp[2]], [ep[0]+step, ep[1], ep[2]])
            self.wait(0.06)
        self.remove(l)
        sp = [3.02, -1.5, 0]
        ep = [-3.02, 1.5, 0]
        l = Line(sp, ep)
        self.add(l)
        for i in range(int(1.5/step)-1):
            sp[1] += step
            ep[1] -= step
            l.put_start_and_end_on([sp[0], sp[1]+step, sp[2]], [ep[0], ep[1]-step, ep[2]])
            self.wait(0.06)
        self.wait(5)
        # self.remove(l)

class Examples(Scene):
    def construct(self):
        main_brownie = ImageMobject("media/images/Main/Brownie.png").rotate(PI / 2).scale(1.78)
        self.add(main_brownie)
        femboy = ImageMobject("media/images/Main/femboy.png").move_to([5, -1, 0]).scale(0.8)
        self.add(femboy)
        self.add(Circle(radius=0.06, color=BLUE, fill_opacity=1))

        for i in range(4):
            x=2*random.random()-1
            y=2*random.random()-1
            main_brownie = Rectangle(width=1.2*np.random.randn(), height=0.60*np.random.randn(), color=BLACK, fill_opacity=1).rotate(2*PI*np.random.randn()).move_to([x,y, 0])
            self.play(Create(main_brownie))
            self.add(Circle(radius=0.06, color=BLUE, fill_opacity=1))
            circle=Circle(radius=0.06, color=BLUE, fill_opacity=1).move_to([x,y, 0])
            self.play(Create(circle))
            l = Line([x,y, 0], [0, 0, 0])
            m = x/y
            l2 = Line([m * 0.48, 0.48, 0], [m * 1.52, 1.52, 0])
            l3 = Line([m * 0.48, 0.48, 0], [m * -1.52, -1.52, 0])
            self.play(Create(l))
            self.wait(0.2)
            self.play(Create(l2), Create(l3))
            self.wait(0.1)
            self.play(FadeOut(main_brownie),Uncreate(circle),Uncreate(l),Uncreate(l3),Uncreate(l2))


        self.wait(10)