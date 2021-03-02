class Synthesizer:
    def __init__(self, name, color, voices, amount_osc, synthesis_method, manufacturer):
        self.name = name
        self.color = color
        self.voices = voices
        self.__amount_osc = amount_osc
        self.__synthesis_method = synthesis_method
        self.__manufacturer = manufacturer

    def play_c(self):        
        print('Ceeee')

    def puls_width_modulation(self):        
        print('Shr')

    @property
    def amount_osc(self):        
        return self.__amount_osc

    @amount_osc.setter
    def amount_osc(self, value):        
        self.__amount_osc = value

    @property
    def synthesis_method(self):        
        return self.__synthesis_method

    @synthesis_method.setter
    def synthesis_method(self, method):        
        self.__synthesis_method = method

    @property
    def manufacturer(self):        
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, company):        
        self.__manufacturer = company


synth_1 = Synthesizer('Machinedrum', 'silver', 16, 16, 'frequency modulation', 'Elektron Music Machines')
synth_2 = Synthesizer('Analog Four', 'black', 4, 2, 'subtractive', 'Elektron Music Machines')


class MyCat:
    def __init__(self, name, color, eye_color, legs, hungry, fav_food, fav_sleep_place):
        self.name = name
        self.color = color
        self.eye_color = eye_color
        self.legs = legs
        self.__hungry = hungry
        self.__fav_food = fav_food
        self.__fav_sleep_place = fav_sleep_place

    def want_eat_at_5am(self):        
        if self.__hungry:
            print('Meow ')

    def want_sleep(self):
        if not self.__hungry:
            print('Zzz')

    @property
    def hungry(self):       
        return self.__hungry

    @hungry.setter
    def hungry(self, value):        
        self.__hungry = value

    @property
    def fav_food(self):        
        return self.__fav_food

    @fav_food.setter
    def fav_food(self, food):       
        self.__fav_food = food

    @property
    def fav_sleep_place(self):
        return self.__fav_sleep_place

    @fav_sleep_place.setter
    def fav_sleep_place(self, place):
        self.__fav_sleep_place = place


cat_1 = MyCat('Zhook', 'black', 'green', 4, True, 'fish', 'wherever under the sun')


class MyBook:
    def __init__(self, subject, name, author, cover, pages, knowledge):
        self.__subject = subject
        self.__name = name
        self.__author = author
        self.cover = cover
        self.pages = pages
        self.knowledge = knowledge

    def lie_on_the_shelf(self):        
        return True if self.__subject == 'belles-lettres' else False

    def give_knowledge(self):
        if self.__subject == 'philosophy':
            self.knowledge += 20

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value


book_1 = MyBook('philosophy', 'dissemination', 'jacques derrida', 'hard', 605, 20)
book_1.author = 'euklid'
book_1.name = 'begins'
book_1.give_knowledge()


class MyCity:
    def __init__(self, name, country, founding_date, population, square, underground=False):
        self.name = name
        self.country = country
        self.founding_date = founding_date
        self.__population = population
        self.__square = square
        self.__underground = underground

    def enlargement(self):
        self.__square += 10
        self.__population += 10000

    def emigration(self):
        if not self.__underground:
            self.__population -= 10000
            self.__square -= 10

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value

    @property
    def underground(self):
        return self.__underground

    @underground.setter
    def underground(self, value):
        self.__underground = value


city_1 = MyCity('minsk', 'belarus', '961', 2000000, 340, True)
city_1.enlargement()


class Oscillator:
    def __init__(self, fine_tune, detune, pwd, sub_osc=False, sub_wave=None, wave='saw', vibrato=False):
        self.fine_tune = fine_tune
        self.detune = detune
        self.pwd = pwd
        self.__sub_osc = sub_osc
        self.__sub_wave = sub_wave
        self.__wave = wave
        self.__vibrato = vibrato

    def sub_puls_wave(self):
        if self.__sub_osc:
            self.__sub_wave = 'pulse'

    def sub_5th(self):
        if self.__sub_osc:
            self.__sub_wave = '5th'

    def high_tone(self):
        if self.fine_tune >= 90:
            print('piiiiiiii')

    def reduce_fine_tune(self):
        self.fine_tune -= 5

    @property
    def sub_osc(self):
        return self.__sub_osc

    @sub_osc.setter
    def sub_osc(self, value):
        self.__sub_osc = value

    @property
    def sub_wave(self):
        return self.__sub_wave

    @sub_wave.setter
    def sub_wave(self, value):
        if self.__sub_osc:
            self.__sub_wave = value

    @property
    def wave(self):
        return self.__wave

    @wave.setter
    def wave(self, form):
        self.__wave = form

    @property
    def vibrato(self):
        return self.__vibrato

    @vibrato.setter
    def vibrato(self, value):
        self.__vibrato = value


osc_1 = Oscillator(63, 0, 7, True, 'pulse', 'triangle')
osc_1.fine_tune = 91
osc_1.reduce_fine_tune()
osc_1.high_tone()