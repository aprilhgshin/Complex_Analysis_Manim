from manimlib.imports import *
from math import sqrt

# Animation and synced audio for Branches Problem video
# April Shin

class BranchesProblem(GraphScene):

    def construct(self):

        self.opening()
        heading = self.checklist(1)
        self.cre(heading)
        self.work_cre()
        self.work_chain()
        self.wait()

    def opening(self):
        filename = "./branch_prob_audio/checklist_cre.m4a"
        self.add_sound(filename)

        open = TextMobject("Computing").scale(1.15).to_corner(UP).to_edge(UP, buff=0.6).to_corner(LEFT)
        openb = TextMobject("$\\textit{l}$'(z)").scale(1.15).set_color(BLUE).next_to(open, RIGHT)
        openc = TextMobject("to verify that $\\textit{l}$ is holomorphic").scale(1.15).next_to(openb, RIGHT)

        t_0 = TextMobject("If $\\textit{l}$ is a branch of log z in G,").scale(0.8).next_to(open, DOWN).to_corner(LEFT).shift(DOWN*1)
        t_1 = TextMobject("then $\\textit{l}$ is holomorphic and $\\textit{l}$'(z) = ${1} \\over {z}$,").scale(0.8).next_to(t_0, DOWN).to_corner(LEFT)
        t_1b = TextMobject(" z $\\in$ G").scale(0.8).set_color(ORANGE).next_to(t_1, DOWN).to_corner(LEFT)
        t_2 = TextMobject("$\\leftarrow$ implies z $\\neq$ 0").set_color(ORANGE).scale(0.7).next_to(t_1b, RIGHT).shift(DOWN*0.03)

        graphList = self.graphG()
        axes = graphList[0]
        dashed_graph = graphList[1]
        graph_label = graphList[2]

        self.play(
            FadeIn(open),
            FadeIn(openb),
            FadeIn(openc)
        )
        self.wait(1.5)

        self.play(
            FadeIn(t_0),
            FadeIn(t_1),
            FadeIn(t_1b),
            FadeIn(t_2),
            FadeIn(axes),
            ShowCreation(dashed_graph),
            FadeIn(graph_label)
        )

        self.wait(1.5)
        self.play(
            FadeOut(open),
            FadeOut(openb),
            FadeOut(openc),
            FadeOut(t_0),
            FadeOut(t_1),
            FadeOut(t_1b),
            FadeOut(t_2),
            FadeOut(axes),
            FadeOut(dashed_graph),
            FadeOut(graph_label)
        )

    def checklist(self, method):

        return_list = []

        title = TextMobject("To compute $\\textit{l}$'(z)...").scale(1.5).to_edge(UP, buff=1.5).to_edge(LEFT, buff=1).set_color(BLUE)
        method_intro = TextMobject("There are").scale(1.2).next_to(title, DOWN).to_corner(LEFT).shift(DOWN*0.3+RIGHT*1)
        method_intro_b = TextMobject("2 methods: ").scale(1.2).set_color(BLUE).next_to(method_intro, RIGHT)
        t_1 = TextMobject("$\\rightarrow$").set_color(BLUE).next_to(method_intro, DOWN).to_corner(LEFT).shift(RIGHT*2+DOWN*0.6)
        t_1b = TextMobject("Verify Cauchy-Riemann Equations (CRE)").next_to(t_1, RIGHT).shift(DOWN*0.03)
        t_2 = TextMobject("$\\rightarrow$").set_color(BLUE).next_to(t_1, DOWN).to_corner(LEFT).shift(RIGHT*2+DOWN*0.35)
        t_2b = TextMobject("Use Chain Rule").next_to(t_2, RIGHT)
        chosen1 = TextMobject("Verify Cauchy-Riemann Equations (CRE)").set_color(GOLD).next_to(t_1, RIGHT).shift(DOWN*0.03)
        chosen2 = TextMobject("Use Chain Rule").set_color(GOLD).next_to(t_2, RIGHT)

        if (method==1):
            self.play(
                FadeIn(title),
                Write(method_intro),
                Write(method_intro_b)
            )
            self.play(
                FadeIn(t_1),
                FadeIn(t_1b)
            )
            self.wait(1.5)
            self.play(
                FadeIn(t_2),
                FadeIn(t_2b)
                )

            self.wait(0.1)
            self.play(
                Transform(t_1b, chosen1)
            )
            self.wait(1.6)
            self.play(
                ApplyMethod(t_1b.to_corner, UP+LEFT),
                FadeOut(title),
                FadeOut(method_intro),
                FadeOut(method_intro_b),
                FadeOut(t_1),
                FadeOut(t_2),
                FadeOut(t_2b)
            )
            return_list = [t_1b]

        elif (method==2):

            return_list = [title, method_intro, method_intro_b, t_1, t_1b, t_2, t_2b]

        return return_list

    def cre(self,heading):
        axes = Axes(y_max=6, x_max=9).set_stroke(DARK_GREY, 1)
        circle1 = Circle().set_stroke(DARKER_GREY, 2).scale(2)
        circle2 = Circle().set_stroke(DARKER_GREY, 2).scale(3)
        circle3 = Circle().set_stroke(DARKER_GREY, 2).scale(4)
        circle4 = Circle().set_stroke(DARKER_GREY, 2).scale(5)
        circle5 = Circle().set_stroke(DARKER_GREY, 2).scale(6)
        circle6 = Circle().set_stroke(DARKER_GREY, 2).scale(7)


        t_0 = TextMobject("r ${du \\over dr}$ = ${dv \\over d\\theta}$").scale(1.2).shift(LEFT*2+UP*0.01)
        t_1 = TextMobject("${du \\over d\\theta}$ = -r ${dv \\over dr}$").scale(1.2).next_to(t_0, RIGHT).shift(RIGHT*1)
        self.wait(1.3)
        self.play(
            FadeIn(axes),
            FadeIn(circle1),
            FadeIn(circle2),
            FadeIn(circle3),
            FadeIn(circle4),
            FadeIn(circle5)
        )
        self.wait(0.3)
        self.play(
            Write(t_0))
        self.wait(2)
        self.play(
            Write(t_1)
        )
        self.wait(1.6)
        self.play(
            FadeOut(axes),
            FadeOut(circle1),
            FadeOut(circle2),
            FadeOut(circle3),
            FadeOut(circle4),
            FadeOut(circle5),
            FadeOut(t_0),
            FadeOut(t_1),
            FadeOut(heading[0])
        )

    def work_cre(self):
        filename = "./branch_prob_audio/work_cre.m4a"
        self.add_sound(filename)

        # Heading
        t_0 = TextMobject("$\\textit{l}$ is a branch of log z $\\rightarrow$").to_corner(UP+LEFT)
        t_1 = TextMobject("u(z) = ln|z| ,").set_color(BLUE).next_to(t_0, RIGHT).shift(RIGHT)
        t_2 = TextMobject("v(z) = arg z").set_color(BLUE).next_to(t_1, RIGHT).shift(RIGHT*0.3)

        # First line after heading
        t_3 = TextMobject("r ${du \\over dr}$").to_corner(LEFT).shift(RIGHT*2.5+UP*0.8)
        t_3b = TextMobject("=").next_to(t_3, RIGHT)
        t_3c = TextMobject("${dv \\over d\\theta}$").next_to(t_3b, RIGHT)
        t_3b_copy = TextMobject("=").next_to(t_3, RIGHT)

        t_4 = TextMobject("${du \\over d\\theta}$").next_to(t_3c, RIGHT).shift(RIGHT*2.7)
        t_4b = TextMobject("=").next_to(t_4, RIGHT)
        t_4c = TextMobject("-r ${dv \\over dr}$").next_to(t_4b, RIGHT)
        t_4b_copy = TextMobject("=").next_to(t_4, RIGHT)

        # Second line after heading
        t_5 = TextMobject("r $\\cdot$").to_corner(LEFT).shift(RIGHT*2.35+DOWN*0.2)
        t_5b = TextMobject("${1 \\over r}$").set_color(BLUE).next_to(t_5, RIGHT).shift(LEFT*0.06)
        t_5c = TextMobject("1").set_color(BLUE).next_to(t_5b, RIGHT).shift(RIGHT*0.85)

        t_6 = TextMobject("0").set_color(BLUE).next_to(t_5c, RIGHT).shift(RIGHT*3)
        t_6b = TextMobject("-r $\\cdot$").next_to(t_6, RIGHT).shift(RIGHT*0.7)
        t_6c = TextMobject("0").set_color(BLUE).next_to(t_6b, RIGHT).shift(UP*0.03)

        t_5b.shift(UP*1)
        t_5c.shift(UP*1)
        t_6.shift(UP*1)
        t_6c.shift(UP+LEFT*0.2)

        # Third Line after heading.next_to(t_3, RIGHT)
        t_7 = TextMobject("=").next_to(t_3, RIGHT).shift(DOWN*1)
        t_7b = TextMobject("1").next_to(t_7, LEFT).shift(LEFT*0.1)
        t_7c = TextMobject( "1").next_to(t_7, RIGHT).shift(RIGHT*0.1)

        t_8 = TextMobject("=").next_to(t_4, RIGHT).shift(DOWN*1)
        t_8b = TextMobject("0").next_to(t_8, LEFT).shift(LEFT*0.1)
        t_8c = TextMobject("0").next_to(t_8, RIGHT).shift(RIGHT*0.1)

        t_9a = TextMobject("$\\checkmark$").next_to(t_7c, RIGHT).shift(DOWN).set_color(GOLD)
        t_9b = TextMobject("$\\checkmark$").next_to(t_8c, RIGHT).shift(DOWN).set_color(GOLD)

        return_list = self.checklist(2)
        title = return_list[0]
        method_intro = return_list[1]
        method_intro_b = return_list[2]
        t_1_c = return_list[3]
        t_1b_c = return_list[4]
        t_2_c = return_list[5]
        t_2b_c = return_list[6]

        self.play(Write(t_0))
        self.play(
            FadeIn(t_1),
            FadeIn(t_2)
        )

        self.wait(2.95)

        self.play(
            # "From this..."
            FadeIn(t_3),
            FadeIn(t_4),
            FadeIn(t_3b),
            FadeIn(t_3c),
            FadeIn(t_4b),
            FadeIn(t_4c),
            ApplyMethod(t_3b_copy.shift, DOWN*1),
            ApplyMethod(t_4b_copy.shift, DOWN*1),
        )
        self.play(
            # "We get that..."
            FadeIn(t_5),
            ApplyMethod(t_5b.shift, DOWN)
        )

        self.wait(1)

        self.play(
            FadeIn(t_6b),
            ApplyMethod(t_6c.shift, DOWN+RIGHT*0.2),
            ApplyMethod(t_6.shift, DOWN),
        )

        self.wait(2)

        self.play(
            ApplyMethod(t_5c.shift, DOWN*1)
        )

        self.wait()
        self.play(
            ApplyMethod(t_7.shift, DOWN),
            ApplyMethod(t_7b.shift, DOWN),
            ApplyMethod(t_7c.shift, DOWN),
            ApplyMethod(t_8.shift, DOWN),
            ApplyMethod(t_8b.shift, DOWN),
            ApplyMethod(t_8c.shift, DOWN),
        )

        self.wait(0.5)
        self.play(
            FadeIn(t_9a),
            FadeIn(t_9b)
        )

        self.wait(1.3)

        self.play(
            FadeOut(t_0),
            FadeOut(t_1),
            FadeOut(t_2),
            FadeOut(t_3),
            FadeOut(t_4),
            FadeOut(t_3b),
            FadeOut(t_3c),
            FadeOut(t_4b),
            FadeOut(t_4c),
            FadeOut(t_3b_copy),
            FadeOut(t_4b_copy),
            FadeOut(t_5),
            FadeOut(t_5b),
            FadeOut(t_6b),
            FadeOut(t_6c),
            FadeOut(t_6),
            FadeOut(t_5c),
            FadeOut(t_7),
            FadeOut(t_7b),
            FadeOut(t_7c),
            FadeOut(t_8),
            FadeOut(t_8b),
            FadeOut(t_8c),
            FadeOut(t_9a),
            FadeOut(t_9b),

            FadeIn(title),
            FadeIn(method_intro),
            FadeIn(method_intro_b),
            FadeIn(t_1_c),
            FadeIn(t_1b_c),
            FadeIn(t_2_c),
            FadeIn(t_2b_c)
        )

        filename2 = "./branch_prob_audio/chain.m4a"
        self.add_sound(filename2)

        t_2b_c.set_color(GOLD)
        self.play(
            ApplyMethod(t_2b_c.to_corner, UP+LEFT),
            FadeOut(title),
            FadeOut(method_intro),
            FadeOut(method_intro_b),
            FadeOut(t_1_c),
            FadeOut(t_2_c),
            FadeOut(t_1b_c)
        )


    def work_chain(self):


        t_0 = TextMobject("$\\forall$z $\\in$ G, ").shift(UP*2+LEFT*5)
        t_0b = TextMobject("$e^{\\textit{l}(z)}$").next_to(t_0,RIGHT).shift(RIGHT*3)
        t_0c = TextMobject("=").next_to(t_0b, RIGHT).shift(DOWN*0.03)
        t_0d = TextMobject("z").next_to(t_0c, RIGHT)


        t_1 = TextMobject("=").next_to(t_0c, DOWN).shift(DOWN)
        t_1b = TextMobject("${d \\over dz}(e^{\\textit{l}(z)})$").next_to(t_1, LEFT)
        t_1c = TextMobject("So").next_to(t_1b, LEFT).shift(LEFT*0.2)
        t_1d = TextMobject(" $d \\over dz$(z) = 1").next_to(t_1, RIGHT)
        t_1b_transform = TextMobject("${d \\over dz}(e^{\\textit{l}(z)})$").set_color(RED).next_to(t_1, LEFT)

        t_2 = TextMobject("$\\textit{l}$'(z)$e^{\\textit{l}(z)}$").next_to(t_1b, DOWN).set_color(RED).shift(DOWN*0.4)

        t_3 = TextMobject("So").next_to(t_1c, DOWN).shift(DOWN*2.1)
        t_3b = TextMobject("$\\textit{l}$'(z) = $1 \\over e^{\\textit{l}(z)}$ = $1 \\over z$").next_to(t_3, RIGHT).shift(RIGHT*0.2)

        brace = Brace(t_1b).set_color(RED)


        self.play(
            FadeIn(t_0),
            FadeIn(t_0b),
            FadeIn(t_0c),
            FadeIn(t_0d)
        )
        self.wait(1.3)

        self.play(
            FadeIn(t_1),
            FadeIn(t_1b),
            FadeIn(t_1c),
            FadeIn(t_1d),
        )

        self.wait(0.19)

        self.play(
            FadeIn(brace),
            Transform(t_1b, t_1b_transform),
            FadeIn(t_2))

        self.wait(0.8)
        self.play(
            FadeIn(t_3),
            FadeIn(t_3b),
        )

        self.wait(5)


    def graphG(self):
        axes = Axes(x_min=-3.5, x_max=5).scale(0.7).set_stroke(GREY, 2).shift(RIGHT*2.7).shift(DOWN*0.7)

        exc_line = Arrow(RIGHT, LEFT).set_stroke(BLUE, 8).set_width(3).shift(LEFT*1.4)#((-4,0,0), (0,0,0), color=BLUE).set_stroke(BLUE, 8)

        x_G = [0+1, 1+1, 2+1, 3+1, 2+1, 1+1, 0+1, -1.5, -2, -2.25, -2, -1.5, -0.5, 0, 0.5, 1, 0.5, 0, -0.5, -1.5, -2, -2.25, -2, -1, 1]
        y_G = [3, sqrt(8), sqrt(5), 0, -sqrt(5), -sqrt(8), -3, -3, -2.5,-2, -1.5, -1, -1, -1, -0.75, 0, 0.75, 1, 1, 1, 1.5, 2, 2.5, 3, 3 ]

        coords = [[px,py] for px,py in zip(x_G,y_G)]
        # |
        # V
        points = self.get_points_from_coords(axes,coords)

        dots = self.get_dots_from_coords(axes,coords)
        graph = SmoothGraphFromSetPoints(points,color=ORANGE).set_stroke(ORANGE, 5)
        dashed_graph = DashedVMobject(graph).shift(RIGHT*0.15)
        graph_label = TextMobject("G").shift(RIGHT*2.8 + UP*1.5).set_color(RED).shift(RIGHT*3)

        return [axes, dashed_graph, graph_label]


    def get_points_from_coords(self,axes,coords):
        return [axes.coords_to_point(px,py)
            for px,py in coords
            ]

    def get_dots_from_coords(self,axes,coords,radius=0.1):
        points = self.get_points_from_coords(axes,coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)
