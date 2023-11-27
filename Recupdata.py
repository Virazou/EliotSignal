import pandas as pd
import soundfile as sf

_SAMPLING_RATE = 160000
df = pd.read_parquet('\atco2_corpus_1h\data\test-00000-of-00001-112f39d2f116a22b.parquet')

for index, row in df.iterrows():
    audio_data = row['audio']  # Remplacez 'votre_colonne_audio' par le nom de la colonne contenant les données audio
    output_path = f'enregistrement_{index}.wav'  # Spécifiez le chemin de sortie pour le fichier audio WAV
    
    # Écrivez les données audio au format WAV
    sf.write(output_path, audio_data, _SAMPLING_RATE)  # Utilisez la fréquence d'échantillonnage appropriée (ici '_SAMPLING_RATE' du code que vous avez partagé)


