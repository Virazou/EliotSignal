import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile  # Pour lire un fichier audio
import wave

##Extraction d'un fichier audio

#import pyarrow.parquet as pq
import soundfile as sf
import io
sample_rate = 44100

# # Spécifiez le chemin du fichier Parquet
# parquet_file_path = 'D:\\00 - Documents\SUPAERO\\3A\Cours\PIE\GitHub\EliotSignal\\atco2_corpus_1h\data\\test-00000-of-00001-112f39d2f116a22b.parquet'

# # Lire le fichier Parquet
# table_parquet = pq.read_table(parquet_file_path)

# # Accéder à la colonne "audio" du tableau Parquet
# colonne_audio = table_parquet['audio']

# # Parcourir les enregistrements et extraire les données audio
# for i, enregistrement in enumerate(colonne_audio):
#     # Accéder au champ "bytes" qui contient les données audio binaires
#     donnees_audio_binaires = enregistrement[0].as_py()
    
#     # Accéder au champ "path" qui contient le chemin du fichier audio (peut être ignoré)
#     chemin_audio = enregistrement[1].as_py()

#     # Décoder les données binaires en données audio brutes (vous devrez peut-être adapter le format)
#     # Par exemple, si les données sont en format WAV, utilisez la bibliothèque `soundfile` pour les décodage
#     audio_brut = sf.read(io.BytesIO(donnees_audio_binaires), always_2d=True)

#     # Nom du fichier de sortie (peut également utiliser chemin_audio)
#     nom_fichier_wav = f'enregistrement_{i}.wav'

#     # Enregistrer les données audio brutes au format WAV
#     sf.write(nom_fichier_wav, audio_brut[0], audio_brut[1])

#     print(f'Enregistrement {i} exporté sous {nom_fichier_wav}')



# Lecture du fichier audio
sample_rate, audio_data = wavfile.read('enregistrement_24.wav')

# Calcul de la FFT
fft_result = np.fft.fft(audio_data)

# Calcul des fréquences correspondantes
frequencies = np.fft.fftfreq(len(fft_result), 1.0 / sample_rate)

# On ignore fréquences négatives et on prend seulement la moitié des résultats (car la FFT est symétrique)
positive_frequencies = frequencies[:len(frequencies) // 2]
magnitude = np.abs(fft_result)[:len(frequencies) // 2]

# Tracé du spectre en fréquence initial
plt.figure(figsize=(10, 6))
plt.plot(positive_frequencies, magnitude, label='Spectre initial', color='blue')
plt.title('Spectre en fréquence')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Magnitude')
plt.grid()

# Définir les fréquences de coupure du passe-bande
low_cutoff = 450  # fréquence de coupure inférieure
high_cutoff = 2500 # fréquence de coupure supérieure

# Création d'un filtre passe-bande
filter_indices = np.where((positive_frequencies >= low_cutoff) & (positive_frequencies <= high_cutoff))
fft_result_bandpass = np.zeros_like(fft_result)
fft_result_bandpass[filter_indices] = fft_result[filter_indices]

# Reconstruction du signal filtré en utilisant l'inverse de la FFT
audio_data_bandpass = np.fft.ifft(fft_result_bandpass).real

# Augmentation du volume du signal filtré (amplification)
#amplification_factor = 1.3  # Facteur d'amplification
#audio_data_amplified = audio_data_bandpass * amplification_factor


# Création d'un fichier audio à partir du signal filtré
scaled = np.int16(audio_data_bandpass / np.max(np.abs(audio_data_bandpass)) * 32767)
wavfile.write('audio_filtre_24_V450_2500.wav', sample_rate, scaled)


# Afficher le plot
plt.plot(positive_frequencies, np.abs(fft_result_bandpass)[:len(positive_frequencies)], label='Spectre après filtrage passe-bande', color='red')
plt.legend()
plt.show()


