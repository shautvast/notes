* disassemble into frames `ffmpeg -i lcd.mp4 frames/frame%04d.jpg`
* assemble from frames `ffmpeg -i frames_out/frame%04d.jpg -r 29.97 lcd_out.mp4  `
* extract audio `ffmpeg -i lcd.mkv -vn -acodec copy lcd.mp4`
* merge audio and video `ffmpeg -i lcd_out.mp4 -i lcd.mp4 -acodec copy  out.mp4`
