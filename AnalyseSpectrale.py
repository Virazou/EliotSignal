import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile  # Pour lire un fichier audio

# Lecture du fichier audio
sample_rate, audio_data = wavfile.read('votre_fichier_audio.wav')

# Calcul de la FFT
fft_result = np.fft.fft(audio_data)

# Calcul des fréquences correspondantes
frequencies = np.fft.fftfreq(len(fft_result), 1.0 / sample_rate)

# On ignore fréquences négatives et on prend seulement la moitié des résultats (car la FFT est symétrique)
positive_frequencies = frequencies[:len(frequencies) // 2]
magnitude = np.abs(fft_result)[:len(frequencies) // 2]

# Tracé du spectre en fréquence
plt.figure(figsize=(10, 6))
plt.plot(positive_frequencies, magnitude)
plt.title('Spectre en fréquence')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()