from manimlib.imports import *
import numpy as np

# Animation and synced audio for Linear-Fractional Transformation Example video
# April Shin

class CreateGraph(ComplexTransformationScene):
    CONFIG = {
        "default_apply_complex_function_kwargs":{
                "run_time": 5,
        }
    }

    def construct(self):
        # Manim uses construct() to execute all animation
        self.fact_text()
        questions = self.display_question()
        self.edit_background_plane()
        self.transform_circle_real(questions, 1)
        self.transform()


    def display_question(self):
        # Presents example question to be solved in this video

        # Audio for displaying question
        filename = "./audio_files2/question.m4a"
        self.add_sound(filename)

        # Text to display for question scene
        first_line_q = TextMobject("Exhibit the linear-fractional transformation that maps")
        second_line_q = TextMobject("the unit circle \{z: |z| = 1\} to the real axis.")
        first_line_q.bg = BackgroundRectangle(first_line_q, fill_opacity=1)
        first_line_group = VGroup(first_line_q.bg, first_line_q)
        second_line_q.bg = BackgroundRectangle(second_line_q, fill_opacity=1)
        second_line_group = VGroup(second_line_q.bg, second_line_q)
        second_line_group.next_to(first_line_group, DOWN)

        self.add(first_line_group, second_line_group)

        self.wait(2)
        self.play(
            ApplyMethod(first_line_group.shift, 3*UP),
            ApplyMethod(second_line_group.shift, 3*UP)
        )

        # Returns Mobjects to FadeOut in sync with next scene
        return first_line_group, second_line_group

    def fact_text(self):
        # Opening video with fact on Linear Fractional transformations

        # Audio for opening scene
        filename = "./audio_files2/opening.m4a"
        self.add_sound(filename)

        # Text to display
        rect = Rectangle(fill_color=BLACK, fill_opacity=1, height=10, width=20)
        t_0 = TextMobject("Linear-Fractional Transformations").to_edge(UP, buff=2).scale(1.5)
        t_1 = TextMobject("can be expressed as a composition").to_edge(UP, buff=3.3)
        t_2 = TextMobject("of the elementary transformations: ")
        t_3 = TextMobject("Inversion").scale(0.9).set_color(YELLOW).to_edge(UP, buff=5.3)
        t_4 = TextMobject("Rotation").scale(0.9).set_color(YELLOW)
        t_5 = TextMobject("Translation").scale(0.9).set_color(YELLOW)
        t_2.next_to(t_1, DOWN)
        t_4.next_to(t_3, DOWN)
        t_5.next_to(t_4, DOWN)

        self.add(rect)
        self.add(t_0)
        self.wait(1.45)

        self.play(
            FadeIn(t_1),
            FadeIn(t_2)
        )
        self.wait(1.68)
        self.play(
            FadeIn(t_3),
            FadeIn(t_4),
            FadeIn(t_5)
        )
        self.wait()

        self.play(
            FadeOut(t_0),
            FadeOut(t_1),
            FadeOut(t_2),
            FadeOut(t_3),
            FadeOut(t_4),
            FadeOut(t_5)
        )
        self.remove(rect)


    def edit_background_plane(self):
        # Background coordinate grid
        self.background.set_stroke(GREY, 2)
        self.background.set_stroke(DARK_GREY, 1)
        self.background.unit_size= 1
        self.add_foreground_mobject(self.background.coordinate_labels)


    def transform_circle_real(self, questions, beginning):
        '''
        Displays transformation of circle to real axis
        (Used for beginning and ending of video)

        params:
        questions: list of Mobjects to FadeOut in sync with transformation
        beginning: boolean value for whether method is used beginning or ending of video
        '''

        # Mobjects used for display
        arc = Circle(color = RED, radius=1)

        dot_neg_one = Dot(color=YELLOW,radius=0.08).shift(LEFT*1)
        dot_pos_one = Dot(color=WHITE,radius=0.08).shift(RIGHT*1)
        dot_i = Dot(color=WHITE,radius=0.08).shift(UP*1)
        dot_neg_i = Dot(color=WHITE,radius=0.08).shift(DOWN*1)

        real_line = Line((-8,0,0), (8,0,0), color=RED)
        real_dot_1 = Dot(color=WHITE,radius=0.08)
        real_dot_i = Dot(color=WHITE,radius=0.08).shift(RIGHT*0.5)
        real_dot_neg_i = Dot(color=WHITE,radius=0.08).shift(LEFT*0.5)
        real_neg_one = Dot(color=WHITE,radius=0.08).shift(RIGHT*9)

        self.play(
            FadeIn(arc),
            FadeIn(dot_neg_one),
            FadeIn(dot_pos_one),
            FadeIn(dot_i),
            FadeIn(dot_neg_i)
        )

        if beginning:
            self.wait(1.5)

        self.play(
            Transform(arc, real_line),
            Transform(dot_neg_one, real_neg_one),
            Transform(dot_pos_one, real_dot_1),
            Transform(dot_i, real_dot_i),
            Transform(dot_neg_i, real_dot_neg_i)
        )

        if beginning:
            self.play(
                FadeOut(questions[0]),
                FadeOut(questions[1]),
                FadeOut(arc),
                FadeOut(dot_neg_one),
                FadeOut(dot_pos_one),
                FadeOut(dot_i),
                FadeOut(dot_neg_i),
                FadeOut(real_line),
                FadeOut(real_dot_1),
                FadeOut(real_dot_i),
                FadeOut(real_dot_neg_i),
                FadeOut(real_neg_one),
            )
        else:
            self.play(
                FadeIn(questions[1]),
                ApplyMethod(questions[0].shift, DOWN*2.6),
                FadeOut(self.background),
                FadeOut(arc),
                FadeOut(dot_neg_one),
                FadeOut(dot_pos_one),
                FadeOut(dot_i),
                FadeOut(dot_neg_i),
                FadeOut(real_line),
                FadeOut(real_dot_1),
                FadeOut(real_dot_i),
                FadeOut(real_dot_neg_i),
                FadeOut(real_neg_one),
            )


    def transform(self):
        # Displays step by step transformation of unit circle to real axis and ends with quick transformation from unit circle to real axis

        # Beginning with display of a unit circle
        arc = Circle(color = RED, radius=1)

        # Four points on unit circle
        dot_neg_one = Dot(color=YELLOW,radius=0.08).shift(LEFT*1)
        dot_pos_one = Dot(color=WHITE,radius=0.08).shift(RIGHT*1)
        dot_i = Dot(color=WHITE,radius=0.08).shift(UP*1)
        dot_neg_i = Dot(color=WHITE,radius=0.08).shift(DOWN*1)

        # Unit circle will transform to this vertical line
        line = Line((0.5,-8,0), (0.5,8,0), color=RED)

        # Text to display for tranformation: inversion
        t_0 = TextMobject("First Transformation:").to_corner(UP+LEFT).scale(1.2).to_edge(LEFT, buff=0.4)
        t_1 = TextMobject("Inversion").next_to(t_0, DOWN).set_color(YELLOW).to_corner(UP+LEFT).to_edge(UP, buff=1.2)
        equation1 = TexMobject("f_{1}(z) = {1 \\over z+1}").to_edge(RIGHT, buff=1.7).to_edge(UP, buff=3)
        sub1 = TexMobject("f_{1}(-1) = \\infty").to_edge(UP, buff=3.6)
        sub1.next_to(equation1, DOWN)

        # audio for entire transformation
        first_file = "./audio_files2/transformations.m4a"
        self.add_sound(first_file)

        self.play(FadeIn(t_0))
        self.play(
            ShowCreation(arc),
            ShowCreation(dot_neg_one),
            ShowCreation(dot_pos_one),
            ShowCreation(dot_i),
            ShowCreation(dot_neg_i)
        )
        self.wait(1.8)
        self.play(Write(t_1))
        self.wait(0.45)
        self.play(Write(sub1))
        self.wait(3.5)
        self.play(Write(equation1))

        # Visible points on vertical line mapped from unit circle
        new_dot_pos_one = Dot(color=WHITE,radius=0.08).shift(RIGHT*0.5)
        new_dot_i = Dot(color=WHITE,radius=0.08).shift(DOWN*0.5+RIGHT*0.5)
        new_dot_neg_i = Dot(color=WHITE,radius=0.08).shift(UP*0.5+RIGHT*0.5)

        self.wait(4)
        self.play(
            Transform(arc, line),
            Transform(dot_pos_one, new_dot_pos_one),
            Transform(dot_i, new_dot_i),
            Transform(dot_neg_i, new_dot_neg_i),
            ApplyMethod(dot_neg_one.shift, UP*5)
        )
        self.wait(7)

        self.play(
            FadeOut(t_1),
            FadeOut(sub1),
            ApplyMethod(equation1.shift, UP*1.3),
        )

        # Text to display for preparing for second transformation: Rotation
        t_2 = TextMobject("Second Transformation:").to_corner(UP+LEFT).scale(1.2).to_edge(LEFT, buff=0.4)
        rot = TextMobject("Rotation").next_to(t_0, DOWN).set_color(YELLOW).to_corner(UP+LEFT).to_edge(UP, buff=1.2)
        func_f_1 = TexMobject("f_{1})(z) = {1 \\over z+1}").to_edge(RIGHT, buff=1.7).to_edge(UP, buff=3).shift(UP*1.3)
        func_f_2 = TexMobject("(f_{2} \\circ ").set_color(YELLOW).next_to(func_f_1, LEFT)

        self.play(
            Transform(t_0, t_2),
        )
        equation2_a = TexMobject("*").next_to(equation1, RIGHT).set_color(YELLOW)
        equation2_b = TexMobject("i").next_to(equation2_a, RIGHT).set_color(YELLOW)
        self.play(
            Write(rot),
            Transform(equation1, func_f_1),
            Write(func_f_2),
            Write(equation2_a),
            Write(equation2_b)
        )

        # Vertical line will transform to this horizontal line
        new_line = Line((-8,0.5,0), (8,0.5,0), color=RED)

        # Points mapped to new horizontal line
        line_dot_1 = Dot(color=WHITE,radius=0.08).shift(UP*0.5)
        line_dot_i = Dot(color=WHITE,radius=0.08).shift(UP*0.5+RIGHT*0.5)
        line_dot_neg_i = Dot(color=WHITE,radius=0.08).shift(UP*0.5+LEFT*0.5)

        self.play(
            Transform(arc, new_line),
            Transform(dot_pos_one, line_dot_1),
            Transform(dot_i, line_dot_i),
            Transform(dot_neg_i, line_dot_neg_i),
        )

        self.wait(3)

        # Text to display for last transformation: Translation
        t_3 = TextMobject("Third Transformation:").to_corner(UP+LEFT).scale(1.2).to_edge(LEFT, buff=0.4)
        tra = TextMobject("Translation").next_to(t_0, DOWN).set_color(YELLOW).to_corner(UP+LEFT).to_edge(UP, buff=1.2)
        equation_new = TexMobject("f_{2} \\circ f_{1})(z) = {i \\over z+1}").to_edge(RIGHT, buff=1.7).to_edge(UP, buff=3).shift(UP*1.3)
        equation_tra1 = TexMobject("-").next_to(equation_new, RIGHT).set_color(YELLOW)
        equation_tra2 = TexMobject("{1 \\over 2}i").next_to(equation_tra1, RIGHT).set_color(YELLOW)
        func_f_3 = TexMobject("(f_{3} \\circ ").set_color(YELLOW).next_to(equation_new, LEFT)

        self.wait(3.6)
        self.remove(rot)

        real_line = Line((-8,0,0), (8,0,0), color=RED)
        real_dot_1 = Dot(color=WHITE,radius=0.08)
        real_dot_i = Dot(color=WHITE,radius=0.08).shift(RIGHT*0.5)
        real_dot_neg_i = Dot(color=WHITE,radius=0.08).shift(LEFT*0.5)

        self.play(
            Transform(t_0, t_3),
            Write(tra),
            FadeOut(func_f_2),
            FadeOut(equation2_a),
            FadeOut(equation2_b),
            Transform(equation1, equation_new),
            Write(func_f_3),
            Write(equation_tra1),
            Write(equation_tra2)
        )
        self.wait(1.5)
        final_funct = TexMobject("(f_{3} \\circ f_{2} \\circ f_{1})(z) = {i \\over z+1} - {1 \\over 2}i").shift(UP*2.5)
        final_text = TextMobject("Linear-Fractional Transformation").shift(UP*1.6).scale(1.5)

        # Displaying transformed graph from horizontal line to real line
        self.play(
            Transform(arc, real_line),
            Transform(dot_pos_one, real_dot_1),
            Transform(dot_i, real_dot_i),
            Transform(dot_neg_i, real_dot_neg_i)
        )

        # Audio for ending video
        filename = "./audio_files2/End.m4a"
        self.add_sound(filename)

        self.play(
            FadeOut(equation1),
            FadeOut(func_f_3),
            FadeOut(equation_tra1),
            FadeOut(equation_tra2),
            FadeOut(tra),
            FadeOut(t_0),
            FadeOut(arc),
            FadeOut(dot_neg_one),
            FadeOut(dot_pos_one),
            FadeOut(dot_i),
            FadeOut(dot_neg_i),
        )
        self.wait(0.6)
        self.play(
            Write(final_funct),
        )

        # Displaying summary of transformation (unit circle to real axis)
        self.transform_circle_real([final_funct, final_text], 0)
