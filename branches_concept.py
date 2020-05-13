from manimlib.imports import *
from math import sqrt

# Animation and synced audio for Branches Concept video
# April Shin

class BranchesConcept(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 5,
        "y_min" : 0,
        "y_max" : 6,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "x_labeled_nums" : [0,2,3]
    }
    def construct(self):
        text = self.titleScreen()
        self.case(text)
        self.ending()
        self.wait()


    def titleScreen(self):
        # First scene of video introducing definition of Branches of log z

        # Audio of first scene
        filename = "./branch_concept_audio/opening.m4a"
        self.add_sound(filename)

        # Text to display on first scene
        t_0 = TextMobject("Definition of ").to_edge(UP, buff=2).shift(LEFT*3).scale(1.5)
        t_0a = TextMobject("Branches of log z").scale(1.5).next_to(t_0, RIGHT).set_color(BLUE).shift(DOWN*0.1)
        t_1 = TextMobject("Let G $\\subseteq \\mathbb{C}$  be an open, connected set.").to_edge(UP, buff=3.3)
        t_2 = TextMobject("We say that").next_to(t_1, DOWN).shift(LEFT*4.3)
        t_2a = TextMobject("$\\textit{l}$").set_color(BLUE).next_to(t_2, RIGHT).shift(UP*0.03)
        t_2b = TextMobject("is a ").next_to(t_2a, RIGHT)
        t_2c = TextMobject(" branch of log z").next_to(t_2b, RIGHT).set_color(BLUE).shift(DOWN*0.03)
        t_2d = TextMobject(" in G if $\\textit{l}:G \\rightarrow \\mathbb{C}$").next_to(t_2c, RIGHT).shift(UP*0.03)
        t_3 = TextMobject("1) $\\textit{l}$ is continuous on G").to_edge(UP, buff=5.3)
        t_4 = TextMobject("2) z $\\in$ G $\\implies e^{\\textit{l}(z)} = z$").next_to(t_3, DOWN).shift(LEFT*0.15)
        t_5 = TextMobject("If $\\textit{l}$ is a branch of log z in G, ")
        t_6 = TextMobject("then $\\textit{l}$ is holomorphic and $\\textit{l}'(z)$ = ${1 \\over z}$, z $\\in$ G").next_to(t_5,DOWN)
        t_7 = TextMobject("Branches of log z").set_color(BLUE).to_edge(UP, buff=2).scale(1.5)

        self.add(t_0)
        self.add(t_0a)
        self.wait(0.5)
        self.play(FadeIn(t_1))
        self.wait(2)
        self.play(
            FadeIn(t_2),
            FadeIn(t_2a),
            FadeIn(t_2b),
            FadeIn(t_2c),
            FadeIn(t_2d),
        )
        self.wait(2.5)
        self.play(FadeIn(t_3))
        self.wait(1)
        self.play(FadeIn(t_4))
        self.wait(3)

        self.play(
            FadeOut(t_0),
            Transform(t_0a, t_7),
            FadeOut(t_1),
            FadeOut(t_2),
            FadeOut(t_2a),
            FadeOut(t_2b),
            FadeOut(t_2c),
            FadeOut(t_2d),
            FadeOut(t_3),
            FadeOut(t_4),
            FadeIn(t_5),
            FadeIn(t_6)
        )
        self.wait(6)

        # Returning few Mobjects to change display in other scenes
        return [t_0a, t_5, t_6]

    def case(self, text):
        # Introducing proof topic

        # Proof intro audio
        filename = "./branch_concept_audio/illustration.m4a"
        self.add_sound(filename)

        # Fading out Mobjects from first scene for smooth transition
        self.play(
            FadeOut(text[0]),
            FadeOut(text[1]),
            FadeOut(text[2])
        )

        # Text to display
        t_0 = TextMobject("Case: $z_{0}$ $\\not\\in$ ").to_corner(UP+LEFT).shift(RIGHT*2).shift(DOWN*2)
        t_1 = TextMobject("{\\bf ($-\\infty, 0$ ]}").next_to(t_0).set_color(WHITE).shift(UP*0.03)
        t_1_transform = TextMobject("{\\bf ($-\\infty, 0$ ]}").next_to(t_0).set_color(BLUE).shift(UP*0.03)
        t_2 = TextMobject("Fix $z_{0} \\in G$").scale(0.85).next_to(t_0, DOWN).to_corner(LEFT).shift(DOWN*0.4).shift(RIGHT*2)
        t_1a = TextMobject("Denote as").next_to(t_1, DOWN).shift(RIGHT*1).scale(0.65).set_color(BLUE)
        t_1b = TextMobject("I").set_color(BLUE).next_to(t_1a)
        t_3 = TextMobject("Want to show: $\\textit{l}$ is differentiable at $z_{0}$").scale(0.85).next_to(t_2, DOWN).to_corner(LEFT).shift(RIGHT*2).shift(DOWN*0.05)

        self.play(Write(t_0))
        self.play(Write(t_1))
        self.wait(2.5)
        self.play(Write(t_2))
        self.wait(0.3)
        self.play(
            Transform(t_1, t_1_transform),
            Write(t_1a),
            Write(t_1b)
        )
        self.wait(2.5)
        self.play(Write(t_3))

        # Retrieving graph visuals from self.graphG() to dislay and sync with proof intro audio
        graphList = self.graphG()
        graph = graphList[0]
        dashed_graph = graphList[1]
        graph_label = graphList[2]
        exc_line = graphList[3]
        open_point = graphList[4]
        axes = graphList[5]
        z_0 = graphList[6]
        r_ball = graphList[7]
        z_0_label = graphList[8]

        # Written description of entire graph
        graph_desc = TextMobject("G$\\textbackslash(-\\infty,0]$ is open so $\\exists$r>0 s.t. $B_{r}(z_{0})\\subseteq$ G$\\textbackslash(-\\infty,0]$").scale(0.8).to_edge(DOWN, buff=0.4)

        self.wait(0.2)
        self.play(
            FadeOut(t_1),
            FadeOut(t_1a),
            FadeOut(t_0),
            FadeOut(t_2),
            FadeOut(t_3),
            FadeIn(axes),
            ApplyMethod(t_1b.shift, LEFT*3),
            ShowCreation(exc_line),
            ShowCreation(open_point),
        )

        self.wait(1.5)
        self.play(
            FadeIn(graph_desc),
            FadeOut(t_1b),
            ShowCreation(dashed_graph),
            FadeIn(graph_label),
        )
        self.wait(1.3)
        self.play(
            ShowCreation(z_0),
            ShowCreation(r_ball),
            FadeIn(z_0_label)
        )
        self.wait(1.7)

        self.play(
            FadeOut(graph_desc),
            FadeOut(dashed_graph),
            FadeOut(graph_label),
            FadeOut(z_0),
            FadeOut(r_ball),
            FadeOut(z_0_label),
            FadeOut(exc_line),
            FadeOut(open_point),
            FadeOut(axes)
        )


    def ending(self):
        # Remaining portion of proof

        # Text to display
        ending1 = TextMobject("We know that Log(z) is a branch of log(z) in $\\mathbb{C}\\textbackslash(-\\infty,0]$").to_corner(LEFT).to_edge(LEFT, buff=1).to_edge(UP, buff=2.3)
        ending2 = TextMobject("and $\\textit{l}$ is a branch of log(z) in $B_{r}(z_{0})$.").next_to(ending1, DOWN).to_corner(LEFT).to_edge(LEFT, buff=1)
        ending3 = TextMobject("So $\\exists$k $\\in\\mathbb{Z}$ s.t.").next_to(ending2, DOWN).to_corner(LEFT).to_edge(LEFT, buff=1)
        ending4 = TextMobject("$\\textit{l}$(z) = Log(z) + 2$\\pi$ik, z$\\in$$B_{r}$($z_{0}$)").to_edge(DOWN,buff=2.5)
        ending5 = TextMobject("Then").to_corner(LEFT).to_edge(LEFT, buff=1).to_edge(DOWN, buff=2.65)
        ending5b = TextMobject("$\\textit{l}$ is differentiable at $z_{0}$ ").next_to(ending5, RIGHT).set_color(BLUE).shift(DOWN*0.03)
        ending5c = TextMobject("because").next_to(ending5b, RIGHT)
        ending6 = TextMobject("Log(z) is differentiable at $z_{0}$ and 2$\\pi$ik is differentiable at $z_{0}$").next_to(ending5, DOWN).to_corner(LEFT).to_edge(LEFT, buff=1)
        ending7 = TextMobject("because it is a constant.").next_to(ending6, DOWN).to_corner(LEFT).to_edge(LEFT, buff=1)

        # Audio for ending proof
        filename = "./branch_concept_audio/ending_even_shorter.m4a"
        self.add_sound(filename)

        self.play(Write(ending1))
        self.wait(4.0)
        self.play(Write(ending2))
        self.wait(0.55)
        self.play(Write(ending3))
        self.wait(1)
        self.play(Write(ending4))
        self.wait(0.5)

        self.play(
            ApplyMethod(ending1.shift, UP*1.55),
            ApplyMethod(ending2.shift, UP*1.55),
            ApplyMethod(ending3.shift, UP*1.55),
            ApplyMethod(ending4.shift, UP*1.55),
            Write(ending5),
            Write(ending5b),
        )

        self.play(
            Write(ending5c),
            Write(ending6)
        )
        self.wait(0.18)
        self.play(Write(ending7))


    def graphG(self):
        # Setting up graph G, excluded interval (-inf, 0], R-ball, and point z_0.

        axes = Axes(x_min=-4, x_max=5).scale(0.7).set_stroke(GREY, 2)
        exc_line = Arrow(RIGHT, LEFT).set_stroke(BLUE, 8).set_color(BLUE).set_width(3).shift(LEFT*1.4)#((-4,0,0), (0,0,0), color=BLUE).set_stroke(BLUE, 8)
        z_0 = Dot(color=WHITE,radius=0.08).shift(RIGHT*1.5+UP*1).set_color(WHITE)
        open_point = Circle(radius=0.1).set_stroke(BLUE, 4).set_fill(WHITE, opacity=0).shift(RIGHT*0.13)
        r_ball = DashedVMobject(Circle(radius=0.62)).shift(RIGHT*1.5+UP*1).set_stroke(YELLOW, 4)
        z_0_label = TextMobject("$z_{0}$").shift(RIGHT*1.55+UP*0.7).set_color(WHITE)

        # Coordinates for graph G
        x_G = [0+1, 1+1, 2+1, 3+1, 2+1, 1+1, 0+1, -1.5, -2, -2.25, -2, -1.5, -0.5, 0, 0.5, 1, 0.5, 0, -0.5, -1.5, -2, -2.25, -2, -1, 1]
        y_G = [3, sqrt(8), sqrt(5), 0, -sqrt(5), -sqrt(8), -3, -3, -2.5,-2, -1.5, -1, -1, -1, -0.75, 0, 0.75, 1, 1, 1, 1.5, 2, 2.5, 3, 3 ]

        # Creating open graph G using coordinates
        coords = [[px,py] for px,py in zip(x_G,y_G)]
        points = self.get_points_from_coords(axes,coords)
        dots = self.get_dots_from_coords(axes,coords)
        graph = SmoothGraphFromSetPoints(points,color=RED).set_stroke(RED, 5)
        dashed_graph = DashedVMobject(graph)
        graph_label = TextMobject("G").shift(RIGHT*2.8 + UP*1.5).set_color(RED)

        # Returning VMobjects to display in sync with audio from other portions of video
        return [graph, dashed_graph, graph_label, exc_line, open_point, axes, z_0, r_ball, z_0_label]


    # More helper functions to create graph G
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

# Class for creating graph G
class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)
