import warnings
warnings.filterwarnings('ignore')

from spleeter.separator import Separator
# Use audio loader explicitly for loading audio waveform :
from spleeter.audio.adapter import AudioAdapter

# Using embedded configuration.
separator = Separator('spleeter:2stems')

separator.separate_to_file('test.mp3', '/test')

# =============================

# async
# # List of input to process.
# audio_descriptors = [...]

# # Batch separation export.
# for i in audio_descriptors:
#     separator.separate_to_file(i, '/path/to/output/directory', synchronous=False)

# # Wait for batch to finish.
# separator.join()


# =============================

# audio_loader = AudioAdapter.default()
# sample_rate = 44100
# waveform, _ = audio_loader.load('/path/to/audio/file', sample_rate=sample_rate)

# # Perform the separation :
# prediction = separator.separate(waveform)