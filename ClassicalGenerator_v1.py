def GenerateMelody(Length, Key, Tonality):
    from numpy import empty
    from random import choice
    MelodicProb, BasicProb = [66, 34]
    Melody = empty(Length, dtype = object)
    HugeScale, LowestNote = ValidNotes(Key, Tonality)
    for i in range(0,len(Melody) -1):
        if i == 0:
            FullAvailNotes = Triad(Tonality, LowestNote)
            FirstNoteCand =  [FirstNoteCand for FirstNoteCand in FullAvailNotes if 60 < FirstNoteCand <= max(HugeScale)]
            Melody[i] =  choice(FirstNoteCand)
        while NextIter == False:
            print(BasicProb)
            NextStep = choice(['step','leap'],1, BasicProb])
            if NextStep = 'step':
                


            elif NextStep = 'leap':

    #Rules for picking sequential tones
    return Melody


def ValidNotes(Key, Tonality):
    from numpy import repeat, tile, add
    LowestNote = SubtractOctave_C2Floor(Key)
    if Tonality == 'major':
        ScaleAdder = [0, 2, 4, 5, 7, 9, 11]
    elif Tonality == 'minor':
        ScaleAdder = [0, 2, 3, 5, 7, 8, 10]
    FullFinal = MusicUnitExpander(ScaleAdder, LowestNote)
    return FullFinal,  LowestNote


def SubtractOctave_C2Floor(Key):
    if Key - 12 < 36:
        return Key
    else:
        return SubtractOctave_C2Floor(Key - 12)

def MusicUnitExpander(MusicalUnit, LowestNote):
    from numpy import repeat, tile, add
    UnitAdder = tile(MusicalUnit,4)
    OctaveScale = repeat([0, 12, 24, 36], len(MusicalUnit))
    FullAdder = add(UnitAdder, OctaveScale)
    FullScale = add(FullAdder, LowestNote)
    FullFinal = [FullFinal for FullFinal in FullScale if FullFinal <= 84]
    return FullFinal

def Triad(ChordTonality, LowestNote):
    if ChordTonality == 'major':
        ChordAdder = [0, 4, 7]
    elif ChordTonality == 'minor':
        ChordAdder = [0, 3, 7]
    FourOctChord = MusicUnitExpander(ChordAdder, LowestNote)
    return FourOctChord
