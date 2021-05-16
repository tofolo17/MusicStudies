class Notes:
    def __init__(self, root, notes=None):
        if notes is None:
            notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.notes = notes
        self.root = root
        root_index = self.notes.index(self.root)
        for _ in range(root_index):
            self.notes.insert(len(self.notes), self.notes[0])
            self.notes.pop(0)


class MusicActions(Notes):
    def __init__(self, root: str):
        super().__init__(root=root)

    def get_scale(self, interval_pattern: list):
        pos = 0
        scale = [self.root]
        notes = self.notes.copy()
        notes.append(self.root)
        for interval in interval_pattern:
            if interval == 'T':
                pos += 2
            else:
                pos += 1
            scale.append(notes[pos])
        return scale

    def get_degrees(self):
        degrees = {
            'Primeiro grau maior': '',
            'Segundo grau menor': '',
            'Segundo grau maior': '',
            'Terceiro grau menor': '',
            'Terceiro grau maior': '',
            'Quarta justa': '',
            'Quarta aumentada (Quinta diminuta)': '',
            'Quinta justa': '',
            'Quinta aumentada (Sexta menor)': '',
            'Sexta maior': '',
            'Sétima menor': '',
            'Sétima maior': ''
        }
        for degree in degrees:
            degrees[degree] = self.notes[list(degrees.keys()).index(degree)]
        for k, v in degrees.items():
            print(f'{k:<40} {v}')

    def get_chord(self, interval_pattern: str):
        patterns = {
            '': [0, 4, 7],
            'M': [0, 4, 7],
            'm': [0, 3, 7],
            'm(b5)': [0, 3, 6],
            '7M': [0, 4, 7, 11],
            '7': [0, 4, 7, 10],
            'm7': [0, 3, 7, 10],
            'm7(b5)': [0, 3, 6, 10],
            '6': [0, 4, 7, 9]
        }  # There's a lot of possibilities
        chord = []
        if interval_pattern in list(patterns.keys()):
            for pos in list(patterns.values())[list(patterns.keys()).index(interval_pattern)]:
                chord.append(self.notes[pos])
            return chord
        else:
            return 'Acorde não encontrado em nossa base de dados.'

    def equivalente_cord_shape(self, capo: int):
        print(self.notes[-capo])

    def get_major_harmonic_field(self, triad: bool):
        scale = self.get_scale(['T', 'T', 'S', 'T', 'T', 'T', 'S'])[:-1]
        harmonic_chord_sequence = [
            '', 'm', 'm', '', '', 'm', 'm(b5)'
        ] if triad else [
            '7M', 'm7', 'm7', '7M', '7', 'm7', 'm7(b5)'
        ]
        for note in scale:
            root = MusicActions(note)
            harmonic_chord = root.get_chord(interval_pattern=harmonic_chord_sequence[scale.index(note)])
            print(harmonic_chord, f'{harmonic_chord[0]}{harmonic_chord_sequence[scale.index(note)]}')
