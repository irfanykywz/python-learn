
rem Using 2stems model
spleeter separate -p spleeter:2stems -o output test.mp3
rem spleeter separate -o audio_output audio_example.mp3 

rem use  4stems model  pretrained 4 stems (vocals / bass / drums / other )
rem spleeter separate -o audio_output -p spleeter:4stems audio_example.mp3

rem use 5 stems (vocals / bass / drums / piano / other) model
rem spleeter separate -o audio_output -p spleeter:5stems audio_example.mp3

rem spleeter option :
rem spleeter:2stems
rem spleeter:4stems
rem spleeter:5stems

rem Using models up to 16kHz:
rem spleeter:2stems-16kHz
rem spleeter:4stems-16kHz 
rem spleeter:5stems-16kHz