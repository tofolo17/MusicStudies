from Classes import MusicActions

root = MusicActions('C')

"""
major = ['T', 'T', 'S', 'T', 'T', 'T', 'S']
minor = ['T', 'S', 'T', 'T', 'S', 'T', 'T']

c_scale = root.get_scale(major)
print(c_scale)
"""

# root.get_degrees()

"""
c_major_chord = root.get_chord('M')
print(c_major_chord)
"""

# root.equivalente_cord_shape(capo=4)


root.get_major_harmonic_field(triad=False)
