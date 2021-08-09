LatinName= {"Hydrogen":"Hydrogenium"

 ,"Helium":"Helium"

 ,"Lithium":"Lithium"

 ,"Beryllium":"Beryllium"

 ,"Boron":"Borium"

 ,"Carbon":"Carbonium"

 ,"Nitrogen":"Nitrogenium"

 ,"Oxygen":"Oxygenium"

 ,"Fluorine":"Fluorum"

 ,"Neon":"Neon"

 ,"Sodium":"Natrium"

 ,"Magnesium":"Magnesium"

 ,"Aluminium":"Aluminium"

 ,"Silicon":"Silicium"

 ,"Phosphorus":"Phosphorus"

 ,"Sulfur":" Sulphur"

 ,"Chlorine":"Chlorum"

 ,"Argon":"Argon"

 ,"Potassium":"Kalium"

 ,"Calcium":"Calcium"

 ,"Scandium":"Scandium"

 ,"Titanium":"Titanium"

 ,"Vanadium":"Vanadium"

 ,"Chromium":"Chromium"

 ,"Manganese":"Manganum"

 ,"Iron":"Ferrum"
 
 ,"Cobalt":"Cobaltum"

 ,"Nickel":"Niccolum"

 ,"Copper":"Cuprum"

 ,"Zinc":"Zincum"

 ,"Gallium":"Gallium"

 ,"Germanium":"Germanium"

 ,"Arsenic":"Arsenicum"

 ,"Selenium":"Selenium"

 ,"Bromine":"Bromum"

 ,"Krypton":"Krypton"

 ,"Rubidium":"Rubidium"

 ,"Strontium":"Strontium"

 ,"Yttrium":"Yttrium"

 ,"Zirconium":"Zirconium"

 ,"Niobium":"Niobium"

 ,"Molybdenum":"Molybdenum"

 ,"Technetium":"Technetium"

 ,"Ruthenium":"Ruthenium"

 ,"Rhodium":"Rhodium"

 ,"Palladium":"Palladium"

 ,"Silver":"Argentum"

 ,"Cadmium":"Cadmium"

 ,"Indium":"Indium"

 ,"Tin":"Stannum"

 ,"Antimony":"Stibium"

 ,"Tellurium":"Tellurium"

 ,"Iodine":"Iodum"

 ,"Xenon":"Xenon"

 ,"Cesium":"Caesium"

 ,"Barium":"Barium"

 ,"Lanthanum":"Lanthanum"

 ,"Cerium":"Cerium"

 ,"Praseodymium":"Praseodymium"

 ,"Neodymium":"Neodymium"

 ,"Promethium":"Promethium"

 ,"Samarium":"Samarium"

 ,"Europium":"Europium"

 ,"Gadolinium":"Gadolinium"

 ,"Terbium":"Terbium"

 ,"Dysprosium":"Dysprosium"

 ,"Holmium":"Holmium"

 ,"Erbium":"Erbium"

 ,"Thulium":"Thulium"

 ,"Ytterbium":"Ytterbium"

 ,"Lutetium":"Lutetium"

 ,"Hafnium":"Hafnium"

 ,"Tantalum":"Tantalum"

 ,"Tungsten":"Wolframium"

 ,"Rhenium":"Rhenium"

 ,"Osmium":"Osmium"

 ,"Iridium":"Iridium"

 ,"Platinum":"Platinum"

 ,"Gold":"Aurum"

 ,"Mercury":"Hydrargyrum"

 ,"Thallium":"Thallium"

 ,"Lead":"Plumbum"

 ,"Bismuth":"Bisemutum"

 ,"Polonium":"Polonium"

 ,"Astatine":"Astatum"

 ,"Radon":"Radon"

 ,"Francium":"Francium"

 ,"Radium":"Radium"

 ,"Actinium":"Actinium"

 ,"Thorium":"Thorium"

 ,"Protactinium":"Protactinium"

 ,"Uranium":"Uranium"

 ,"Neptunium":"Neptunium"

 ,"Plutonium":"Plutonium"

 ,"Americium":"Americium"

 ,"Curium":"Curium"

 ,"Berkelium":"Berkelium"

 ,"Californium":"Californium"

 ,"Einsteinium":"Einsteinium"

 ,"Fermium":"Fermium"

 ,"Mendelevium":"Mendelevium"

 ,"Nobelium":"Nobelium"

 ,"Lawrencium":"Lawrencium"

 ,"Rutherfordium":"Rutherfordium"

 ,"Dubnium":"Dubnium"

 ,"Seaborgium":"Seaborgium"

 ,"Bohrium":"Bohrium"

 ,"Hassium":"Hassium"

 ,"Meitnerium":"Meitnerium"

 ,"Darmstadtium":"Darmstadtium"

 ,"Roentgenium":"Roentgenium"

 ,"Copernicium":"Copernicium"

 ,"Nihonium":"Nihonium"

 ,"Flerovium":"Flerovium"

 ,"Moscovium":"Moscovium"

 ,"Livermorium":"Livermorium"

 ,"Tennessine":"Tennessine"

 ,"Oganesson":"Oganesson"}

from flask import Flask

app = Flask(__name__)


@app.route('/latin/<string:x>')
def latin_name(x):
  y=x.title()
  return (LatinName[y])

if __name__ == '__main__':
  app.run()
