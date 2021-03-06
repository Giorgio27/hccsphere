## http://en.wikipedia.org/wiki/Atomic_radius#Calculated_atomic_radii
## http://en.wikipedia.org/wiki/Atomic_radius#Empirically_measured_atomic_radius
## http://en.wikipedia.org/wiki/Van_der_Waals_radius
## http://en.wikipedia.org/wiki/Covalent_radius

## 0 => No data available
## units = picometers: 1.0 x 10^(-12)

RADIUS_TYPE = 3 # van der Waals

## symbol:(name, empirical, Calculated, van der Waals, covalent)
atomic_radius = {
    "H":("hydrogen",35,53,120,38),
    "He":("helium",0,31,140,32),
    "Li":("lithium",145,167,182,134),
    "Be":("beryllium",105,112,153,90),
    "B":("boron",85,87,192,82),
    "C":("carbon",70,67,170,77),
    "N":("nitrogen",65,56,155,75),
    "O":("oxygen",60,48,152,73),
    "F":("fluorine",50,42,147,71),
    "Ne":("neon",0,38,154,69),
    "Na":("sodium",180,190,227,154),
    "Mg":("magnesium",150,145,173,130),
    "Al":("aluminium",125,118,184,118),
    "Si":("silicon",110,111,210,111),
    "P":("phosphorus",100,98,180,106),
    "S":("sulfur",100,88,180,102),
    "Cl":("chlorine",100,79,175,99),
    "Ar":("argon",71,71,188,97),
    "K":("potassium",220,243,275,196),
    "Ca":("calcium",180,194,231,174),
    "Sc":("scandium",160,184,211,144),
    "Ti":("titanium",140,176,0,136),
    "V":("vanadium",135,171,0,125),
    "Cr":("chromium",140,166,0,127),
    "Mn":("manganese",140,161,0,139),
    "Fe":("iron",140,156,0,125),
    "Co":("cobalt",135,152,0,126),
    "Ni":("nickel",135,149,163,121),
    "Cu":("copper",135,145,140,138),
    "Zn":("zinc",135,142,139,131),
    "Ga":("gallium",130,136,187,126),
    "Ge":("germanium",125,125,211,122),
    "As":("arsenic",115,114,185,119),
    "Se":("selenium",115,103,190,116),
    "Br":("bromine",115,94,185,114),
    "Kr":("krypton",0,88,202,110),
    "Rb":("rubidium",235,265,303,211),
    "Sr":("strontium",200,219,249,192),
    "Y":("yttrium",180,212,0,162),
    "Zr":("zirconium",155,206,0,148),
    "Nb":("niobium",145,198,0,137),
    "Mo":("molybdenum",145,190,0,145),
    "Tc":("technetium",135,183,0,156),
    "Ru":("ruthenium",130,178,0,126),
    "Rh":("rhodium",135,173,0,135),
    "Pd":("palladium",140,169,163,131),
    "Ag":("silver",160,165,172,153),
    "Cd":("cadmium",155,161,158,148),
    "In":("indium",155,156,193,144),
    "Sn":("tin",145,145,217,141),
    "Sb":("antimony",145,133,206,138),
    "Te":("tellurium",140,123,206,135),
    "I":("iodine",140,115,198,133),
    "Xe":("xenon",0,108,216,130),
    "Cs":("caesium",260,298,343,225),
    "Ba":("barium",215,253,268,198),
    "La":("lanthanum",195,0,0,169),
    "Ce":("cerium",185,0,0,0),
    "Pr":("praseodymium",185,247,0,0),
    "Nd":("neodymium",185,206,0,0),
    "Pm":("promethium",185,205,0,0),
    "Sm":("samarium",185,238,0,0),
    "Eu":("europium",185,231,0,0),
    "Gd":("gadolinium",180,233,0,0),
    "Tb":("terbium",175,225,0,0),
    "Dy":("dysprosium",175,228,0,0),
    "Ho":("holmium",175,0,0,0),
    "Er":("erbium",175,226,0,0),
    "Tm":("thulium",175,222,0,0),
    "Yb":("ytterbium",175,222,0,0),
    "Lu":("lutetium",175,217,0,160),
    "Hf":("hafnium",155,208,0,150),
    "Ta":("tantalum",145,200,0,138),
    "W":("tungsten",135,193,0,146),
    "Re":("rhenium",135,188,0,159),
    "Os":("osmium",130,185,0,128),
    "Ir":("iridium",135,180,0,137),
    "Pt":("platinum",135,177,175,128),
    "Au":("gold",135,174,166,144),
    "Hg":("mercury",150,171,155,149),
    "Tl":("thallium",190,156,196,148),
    "Pb":("lead",180,154,202,147),
    "Bi":("bismuth",160,143,207,146),
    "Po":("polonium",190,135,197,0),
    "At":("astatine",0,0,202,0),
    "Rn":("radon",0,120,220,145),
    "Fr":("francium",0,0,348,0),
    "Ra":("radium",215,0,283,0),
    "Ac":("actinium",195,0,0,0),
    "Th":("thorium",180,0,0,0),
    "Pa":("protactinium",180,0,0,0),
    "U":("uranium",175,0,186,0),
    "Np":("neptunium",175,0,0,0),
    "Pu":("plutonium",175,0,0,0),
    "Am":("americium",175,0,0,0),
    "Cm":("curium",0,0,0,0),
    "Bk":("berkelium",0,0,0,0),
    "Cf":("californium",0,0,0,0),
    "Es":("einsteinium",0,0,0,0),
    "Fm":("fermium",0,0,0,0),
    "Md":("mendelevium",0,0,0,0),
    "No":("nobelium",0,0,0,0),
    "Lr":("lawrencium",0,0,0,0),
    "Rf":("rutherfordium",0,0,0,0),
    "Db":("dubnium",0,0,0,0),
    "Sg":("seaborgium",0,0,0,0),
    "Bh":("bohrium",0,0,0,0),
    "Hs":("hassium",0,0,0,0),
    "Mt":("meitnerium",0,0,0,0),
    "Ds":("darmstadtium",0,0,0,0),
    "Rg":("roentgenium",0,0,0,0),
    "Cn":("copernicium",0,0,0,0),
    "Uut":("ununtrium",0,0,0,0),
    "Uuq":("ununquadium",0,0,0,0),
    "Uup":("ununpentium",0,0,0,0),
    "Uuh":("ununhexium",0,0,0,0)
    }

if __name__ == "__main__":
    print atomic_radius['H']
    print atomic_radius['H'][RADIUS_TYPE]
