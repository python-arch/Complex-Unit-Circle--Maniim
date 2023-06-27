# The manim stuff
from manim import *

class ComplexUnitCircle(ThreeDScene):
    def construct(self):
        # some config
        Text.set_default(weight=BOLD)
        # first screen
        rect= Rectangle(BLUE).scale(4).set_stroke(width=3)
        intro = Text("Parametrizing unit circle using the complex exponential functionn (Euler's Formula)").scale(0.52)
        second_text = Text("Seems tough , Huh?")
        self.play(Write(intro), run_time=3)
        self.play(Create(rect))
        self.wait(2)
        self.play(FadeOut(intro))
        # Second Screen
        self.play(Create(second_text) , run_time=1)
        dot= Dot(ORIGIN)
        self.wait()
        self.play(second_text.animate.to_edge(UP))
        self.wait()
        third_text = Text("How about we look at the function?")
        self.play(Create(dot),dot.animate.to_edge(UP), ReplacementTransform(second_text,third_text))
        self.wait(2)
        self.play(FadeOut(third_text, target_position= dot))
        # Third Scene and equation stuff
        equation = Tex("$z = e^{ t \pi i}$").scale(1.1)
        equation2 = Tex("$e^{ t \pi i} = \cos{(\pi t)} + \sin{(\pi t)} i$")
        self.play(ReplacementTransform(dot,equation))
        self.wait()
        self.play(equation.animate.scale(1.5))
        self.play(ReplacementTransform(equation,equation2))
        self.wait(2)
        equation1_2 = Tex("$z = e^{ t \pi i}$").scale(1.5)
        self.play(equation2.animate.set_color(RED))
        self.wait()
        self.play(ReplacementTransform(equation2, equation1_2))
        self.wait(2)
        self.play(equation1_2.animate.to_edge(DOWN))
        self.wait() 
        # Fourth and intro to 3D visuals
        text_i = Text("Still not making sense, How about Visualization?").scale(0.8)
        self.play(Write(text_i) , equation1_2.animate.scale(1.1))
        self.play(equation1_2.animate.next_to(text_i, DOWN, buff=1))
        self.play(equation1_2.animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeOut(text_i), FadeOut(equation1_2), ShowCreationThenFadeOut(rect), run_time=2)
    #    Setting up three D environment
        a = ThreeDAxes(
            z_range=[-10,10]
            ,x_range=[-5,5],
            y_range=[-5,5]
        )
        labels = a.get_axis_labels(
            Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
        )
        # parametric form of the euler equation
        f =ParametricFunction(
            lambda t :[np.cos(t),np.sin(t),0.1*t] ,t_range=(0,9*PI)
        , color= BLUE , stroke_width=5)
        self.set_camera_orientation(phi=70*DEGREES,theta=240*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.02)
        self.play(
            Write(a), Create(f) , Create(labels) ,run_time=2
        )
        self.stop_ambient_camera_rotation()
        c = ParametricFunction(lambda t :[np.cos(t),np.sin(t),0] ,t_range=(0,9*PI) , color= BLUE ,stroke_width=10)
        self.move_camera(theta=120*DEGREES,run_time=6,rate_func=linear)
        self.play(FadeOut(labels))
        self.wait(1)
        # Three D
        threed_text =Text("In 3D Space , The Function Looks Like Spiral").scale(0.48)
        self.add_fixed_in_frame_mobjects(threed_text)
        threed_text.to_corner(UL)
        self.play(Write(threed_text) , run_time=2)
        self.play(threed_text.animate.set_color(BLUE))
        self.wait()
        self.play(FadeOut(threed_text))
        self.play(f.animate.set_stroke_width(1)) 
        # XY plane 
        self.move_camera(theta=180*DEGREES,phi=0,run_time=2,rate_func=smooth, focal_distance=500)
        self.play(f.animate.set_color(GREEN))
        n = NumberPlane(x_range=[-5,5],
            y_range=[-5,5])
        n.set_color(BLUE)
        threed2_text =Text("Moving to XY Plane , Unit Circle Appears").scale(0.5)
        self.add_fixed_in_frame_mobjects(threed2_text)
        threed2_text.to_corner(UL)
        self.play(Write(threed2_text) , run_time=2)
        self.play(threed2_text.animate.set_color(GREEN))
        self.wait(2)
        self.play(FadeOut(threed2_text))
        self.wait()
        self.play(Create(n))
        self.play(ReplacementTransform(f,c))
        self.play(FadeOut(n))
        self.play(Indicate(c))
        self.wait(1)
        # YZ plane
        self.move_camera(theta=180*DEGREES,phi=90*DEGREES,run_time=2, rate_func=smooth)
        f2_1= ParametricFunction(
            lambda t :[np.cos(t),np.sin(t),0.1*t] ,t_range=(0,8*PI)
        , color= BLUE , stroke_width=5)
        self.play(ReplacementTransform(c,f2_1))
        self.play(f2_1.animate.set_color(ORANGE).set_stroke_width(7))
        self.move_camera(phi=90*DEGREES, gamma= -90*DEGREES)
        self.move_camera(phi=90*DEGREES, gamma= -90*DEGREES ,zoom= 2)
        self.wait()
        self.play(FadeOut(f2_1))
        self.play(Write(f2_1), run_time=2)
        threed3_text =Text("Moving to YZ plane , The Sin Component Appears").scale(0.44)
        self.add_fixed_in_frame_mobjects(threed3_text)
        threed3_text.to_corner(UL)
        self.play(Write(threed3_text) , run_time=2)
        self.play(threed3_text.animate.set_color(ORANGE))
        self.wait(2)
        self.play(FadeOut(threed3_text))
        self.wait()
        self.move_camera(phi=90*DEGREES, gamma= -90*DEGREES , zoom=1)
        self.wait()
        # XZ plane
        self.move_camera(theta = 90*DEGREES, zoom=1) 
        self.play(f2_1.animate.set_color(RED), run_time=2)  
        self.move_camera(theta = 90*DEGREES, zoom=2)
        self.wait()
        threed4_text =Text("Moving to XZ plane , The Cos Component Appears").scale(0.44)
        self.add_fixed_in_frame_mobjects(threed4_text)
        threed4_text.to_corner(UL)
        self.play(Write(threed4_text) , run_time=2)
        self.play(threed4_text.animate.set_color(RED))
        self.wait(2)
        self.play(FadeOut(threed4_text))
        self.play(ShowCreationThenFadeOut(f2_1), run_time=3)
        self.move_camera(theta = 90*DEGREES, zoom=1)
        self.move_camera(phi=-60*DEGREES,theta=40*DEGREES , gamma=180*DEGREES)
        self.play(
        Write(labels),run_time=2
        )
        self.play(
        Write(f2_1) ,run_time=2
        )
        self.play(f2_1.animate.set_color(GREEN))
        self.play(Write(n))
        # OUTRO
        dot = Dot(ORIGIN)
        self.play(ReplacementTransform(f2_1,dot))
        self.play(FadeOut(a,n,labels))
        created_by = Text("Developed by A. El Sayed")
        linee = Line(LEFT, RIGHT)
        self.play(ReplacementTransform(dot,linee))
        self.move_camera(theta=90*DEGREES,phi=0,run_time=2,rate_func=smooth)
        self.play(ReplacementTransform(linee,created_by))
        self.play(Indicate(created_by))
        self.play(FadeOut(created_by))
    # Custom method to be implemented later
    def custom_move_camera(self, phi_1 , theta_1 , gamma_1):
        camera_pos = [-(camera_pos[0] - phi_1) ,-( camera_pos[1]-theta_1), -(camera_pos[2]- gamma_1) ]
        self.move_camera(*[camera_pos])
         
    