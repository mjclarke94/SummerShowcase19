from manimlib.imports import *

class Technologies(GraphScene):
    CONFIG = {"y_min": -75,
        "y_max": 600,
        "y_axis_height": 6,
        "y_tick_frequency": 75,
        "x_min": -50,
        "x_max": 400,
        "x_axis_width": 9,
        "x_tick_frequency": 50,
        "x_axis_label": "",
        "y_axis_label": ""}

    def construct(self):
        self.setup_axes(animate=True)
        
        origin = self.coords_to_point(0,0)
        unitx = (self.coords_to_point(1,0) - origin)[0]
        unity = (self.coords_to_point(0,1) - origin )[1]

        xlabel = TextMobject("Lighter $\\rightarrow$")
        xlabel.move_to(self.coords_to_point(350,50))
        xlabel.scale(0.8)

        ylabel = TextMobject("Smaller $\\rightarrow$")
        ylabel.rotate(90*DEGREES)
        ylabel.scale(0.8)
        ylabel.move_to(self.coords_to_point(20,500))
        
        # Lead acid setup
        lead = Circle(fill_color = RED, fill_opacity = 0.8)
        leadx  = 35
        leady = 50

        lead.move_to(self.coords_to_point(leadx, leady))
        lead.scale(18*unitx)
        lead_0=TextMobject("Lead")
        lead_1=TextMobject("acid")
        lead_0.scale(0.4)
        lead_1.scale(0.4)
        lead_1.next_to(lead_0,DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER * 0.5)

        VGroup(lead_0,lead_1).move_to(self.coords_to_point(leadx, leady))

        # NiCd setup
        NiCd = Ellipse(height = 150*unity, width = 50*unitx, color = GREEN, fill_color = GREEN, fill_opacity = 0.8)
        NiCdx  = 70
        NiCdy = 140
        
        NiCd_angle = 20*DEGREES
        NiCd.rotate(-NiCd_angle)
        NiCd.move_to(self.coords_to_point(NiCdx, NiCdy))

        NiCd_0=TextMobject("NiCd")
        NiCd_0.rotate(90*DEGREES - NiCd_angle)
        NiCd_0.scale(0.6)

        NiCd_0.move_to(self.coords_to_point(NiCdx, NiCdy))


        # Ni-Mh setup
        NiMh = Ellipse(height = 230*unity, width = 50*unitx, color = PURPLE, fill_color = PURPLE, fill_opacity = 0.8)
        NiMhx  = 120
        NiMhy = 235
        
        NiMh_angle = 10*DEGREES
        NiMh.rotate(-NiMh_angle)
        NiMh.move_to(self.coords_to_point(NiMhx, NiMhy))

        NiMh_0=TextMobject("Ni-MH")
        NiMh_0.rotate(90*DEGREES - NiMh_angle)
        NiMh_0.scale(0.6)

        NiMh_0.move_to(self.coords_to_point(NiMhx, NiMhy))

        # Li-ion setup
        Li = Ellipse(height = 200*unity, width = 60*unitx, color = BLUE, fill_color = BLUE, fill_opacity = 0.8)
        Lix  = 180
        Liy = 320
        
        Li_angle = 40*DEGREES
        Li.move_to(self.coords_to_point(Lix, Liy))
        Li.rotate(-Li_angle)

        Li_0=TextMobject("Li-ion")
        Li_0.rotate(90*DEGREES - Li_angle)
        Li_0.scale(0.6)

        Li_0.move_to(self.coords_to_point(Lix, Liy))


        goalbase = Ellipse(height = 250*unity, width = 80*unitx, color = "#E62020")
        goal = DashedVMobject(goalbase, num_dashes = 30)
        goal.rotate(-45*DEGREES)
        goal.move_to(self.coords_to_point(300, 500))

        self.wait(2)

        self.play(Write(xlabel), LaggedStart(*map(Write, ylabel)))
        
        self.play(FadeIn(lead))
        self.play(Write(lead_0), Write(lead_1))
        
        self.play(FadeIn(NiCd))
        self.play(Write(NiCd_0))
        
        self.play(FadeIn(NiMh))
        self.play(Write(NiMh_0))

        self.play(FadeIn(Li))
        self.play(Write(Li_0))
        self.play(FadeIn(goal))

class Inside(Scene):
    def construct(self):
        CELL_HEIGHT = 4
        CELL_WIDTH = 8
        ELECTRODE_WIDTH = 3.5
        WIRE_HEIGHT = 0.5

        # Create primitives

        ## Electrode blocks
        cathode_block = Rectangle(height = CELL_HEIGHT,width = ELECTRODE_WIDTH,fill_color=BLUE,fill_opacity=0.8,stroke_width = 0)
        anode_block = Rectangle(height = CELL_HEIGHT,width = ELECTRODE_WIDTH,fill_color=RED,fill_opacity=0.8,stroke_width = 0)
        ##Electrolyte
        electrolyte_block = Rectangle(height=CELL_HEIGHT, width=CELL_WIDTH-2*ELECTRODE_WIDTH,fill_color=GRAY,fill_opacity=0.5,stroke_width=0)

        ## Dividers
        cathode_divider = DashedLine(start=ORIGIN, end=UP*CELL_HEIGHT)
        anode_divider = DashedLine(start=ORIGIN, end=UP*CELL_HEIGHT)

        ## Wires
        wirer = Line(color=RED, start = ORIGIN, end = UP*WIRE_HEIGHT)
        wirel = Line(color=BLUE, start = ORIGIN, end = UP*WIRE_HEIGHT)

        ## Cell
        cell = Rectangle(height=CELL_HEIGHT, width=CELL_WIDTH)

        ## Text
        cathode_text = TextMobject('Cathode')
        cathode_material = TexMobject('LiCoO_2')
        cathode_material.scale(0.8)
        cathode_material.set_color(BLUE)

        anode_text = TextMobject('Anode')
        anode_material = TextMobject('Graphite')
        anode_material.set_color(RED)
        anode_material.scale(0.8)

        electrolyte_text = TextMobject('Electrolyte')
        title = TextMobject("Structure of a lithium-ion battery")

        # Alignment

        cathode_material.next_to(cell, UP + LEFT)
        anode_material.next_to(cell, UP + RIGHT)

        anode_block.align_to(cell,RIGHT)
        cathode_block.align_to(cell,LEFT)

        cathode_divider.align_to(cathode_block,RIGHT)
        cathode_divider.align_to(cell, BOTTOM)
        anode_divider.align_to(anode_block,LEFT)
        anode_divider.align_to(cell, BOTTOM)

        wirel.next_to(cathode_block,UP,0.0)
        wirer.next_to(anode_block,UP,0.0)


        electrolyte_text.next_to(cell,DOWN)
        anode_text.next_to(cell,RIGHT)
        cathode_text.next_to(cell,LEFT)

        all = VGroup(cathode_block, anode_block, cathode_material, anode_material, cathode_text, anode_text, cathode_divider, anode_divider, electrolyte_text, electrolyte_block, cell, wirel, wirer)

        # Make Cathodes


        ATOMSCALE = 1.5
        XSCALE = 1.4
        YSCALE = XSCALE / 2.815 * 14.05
        TEXTSCALE = 1

        Li = []
        O = []
        Co = []

        OFFSET = RIGHT * -6 * XSCALE + UP * -0.5 * YSCALE

        NX = 5
        NY = 1

        hlratio = 14.05/ 2.815



        for x in np.arange(NX):
            for y in np.arange(NY):

                L0 = Atom(species = 'Li', color = GREEN, fill_color = GREEN, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.1 * ATOMSCALE)
                L1 = Atom(species = 'Li', color = GREEN, fill_color = GREEN, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.1 * ATOMSCALE)
                L2 = Atom(species = 'Li', color = GREEN, fill_color = GREEN, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.1 * ATOMSCALE)

                L0.move_to((RIGHT * x) * XSCALE +
                           (UP * y) * YSCALE
                           + OFFSET)

                L1.move_to((RIGHT * (x + 0.6667) * XSCALE +
                           (UP * (y + 0.3333)) * YSCALE
                           + OFFSET))

                L2.move_to((RIGHT * (x + 0.3333) * XSCALE +
                           (UP * (y + 0.6667)) * YSCALE
                           + OFFSET))
                Li.append(L0)
                Li.append(L1)
                Li.append(L2)

                Co0 = Atom(species = 'Co', color = DARK_BLUE, fill_color = DARK_BLUE, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.075 * ATOMSCALE)
                Co1 = Atom(species = 'Co', color = DARK_BLUE, fill_color = DARK_BLUE, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.075 * ATOMSCALE)
                Co2 = Atom(species = 'Co', color = DARK_BLUE, fill_color = DARK_BLUE, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.075 * ATOMSCALE)
                Co0.move_to((RIGHT * (x + 0.3333) * XSCALE +
                           (UP * (y + 0.1667)) * YSCALE
                           + OFFSET))

                Co1.move_to((RIGHT * (x) * XSCALE +
                           (UP * (y + 0.5)) * YSCALE
                           + OFFSET))

                Co2.move_to((RIGHT * (x + 0.6667) * XSCALE +
                           (UP * (y + 0.8333)) * YSCALE
                           + OFFSET))
                Co.append(Co0)
                Co.append(Co1)
                Co.append(Co2)


                O0 = Atom(species = 'O', color = RED, fill_color = RED, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.15 * ATOMSCALE)
                O1 = Atom(species = 'O', color = RED, fill_color = RED, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.15 * ATOMSCALE)
                O2 = Atom(species = 'O', color = RED, fill_color = RED, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.15 * ATOMSCALE)
                O3 = Atom(species = 'O', color = RED, fill_color = RED, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.15 * ATOMSCALE)
                O4 = Atom(species = 'O', color = RED, fill_color = RED, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.15 * ATOMSCALE)
                O5 = Atom(species = 'O', color = RED, fill_color = RED, fill_opacity = 0.8, text_size = 0.3 * TEXTSCALE, radius = 0.15 * ATOMSCALE)
                O0.move_to((RIGHT * (x + 0.6667) * XSCALE +
                           (UP * (y + 0.0939)) * YSCALE
                           + OFFSET))

                O1.move_to((RIGHT * (x) * XSCALE +
                           (UP * (y + 0.2394)) * YSCALE
                           + OFFSET))

                O2.move_to((RIGHT * (x + 0.3333) * XSCALE +
                           (UP * (y + 0.4273)) * YSCALE
                           + OFFSET))
                O3.move_to((RIGHT * (x + 0.6667) * XSCALE +
                           (UP * (y + 0.5727)) * YSCALE
                           + OFFSET))

                O4.move_to((RIGHT * (x) * XSCALE +
                           (UP * (y + 0.7606)) * YSCALE
                           + OFFSET))

                O5.move_to((RIGHT * (x + 0.3333) * XSCALE +
                           (UP * (y + 0.9061)) * YSCALE
                           + OFFSET))
                O.append(O0)
                O.append(O1)
                O.append(O2)
                O.append(O3)
                O.append(O4)
                O.append(O5)

        Li.reverse()
        O.reverse()
        Co.reverse()

        Li = VGroup(*Li)
        Co = VGroup(*Co)
        O = VGroup(*O)

        CathodeAtoms = VGroup(Li, Co, O)

        CathodeAtoms.next_to(cathode_divider, LEFT, 0.5)


        self.play(Write(title))
        self.wait()
        self.play(ApplyMethod(title.move_to, TOP+DOWN*0.5))


        self.play(DrawBorderThenFill(cell))
        self.play(Write(cathode_text), Write(anode_text), ShowCreation(cathode_divider), ShowCreation(anode_divider))

        self.wait()
        self.play(Write(cathode_material),
                  Write(anode_material))
        self.wait()
        self.play(Transform(cathode_material, cathode_block),
                  Transform(anode_material, anode_block))
        self.play(ShowCreation(wirel),ShowCreation(wirer))
        self.wait()
        self.play(Write(electrolyte_text))
        self.wait()
        self.play(Transform(electrolyte_text, electrolyte_block))
        self.wait()
        self.play(ApplyMethod(all.scale,2), FadeOut(title))
        self.wait()
        self.play(ShowCreation(Li), ShowCreation(Co),  ShowCreation(O))
        self.wait()
        self.play(LaggedStart(*[ApplyMethod(L.shift, RIGHT*11) for L in Li], lag_ratio=0.05), run_time=5)
        self.wait()

class Atom(Circle):
    CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        "species": "Li",
        "text_size": 0.7
        }

    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        lab = TextMobject(self.species)
        lab.scale(self.text_size)
        lab.move_to(self)
        self.add(lab)

class MovingTest(ZoomedScene):
    def setup(self):
        ZoomedScene.setup(self)
    def construct(self):
        c = Rectangle(width=8, height = 4)
        d = Square()
        self.play(ShowCreation(c))
        self.play(ShowCreation(d))
        frame = self.zoomed_camera.frame
        frame.move_to(LEFT)
        self.activate_zooming(animate=True)
        self.play(ApplyMethod(mo)