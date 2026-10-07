#!/bin/bash
# Encode masters, side-by-side comparison, and inspection crops.
set -e
cd /home/user/Higg/cp2
mkdir -p out
for v in A B; do
  ffmpeg -y -loglevel error -framerate 24 -i work/$v/f_%04d.png -c:v libx264 -preset slow -crf 14 -pix_fmt yuv420p -movflags +faststart out/cp2_${v}_1080x1920.mp4
done
# side by side (each 540x960) with labels, plus a 1s hold on the last frame
ffmpeg -y -loglevel error -i out/cp2_A_1080x1920.mp4 -i out/cp2_B_1080x1920.mp4 -filter_complex \
"[0:v]scale=540:960,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf:text='A  restrained push/arc':x=18:y=18:fontsize=22:fontcolor=white@0.85,tpad=stop_mode=clone:stop_duration=1[a];\
[1:v]scale=540:960,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf:text='B  beam entry + rack focus':x=18:y=18:fontsize=22:fontcolor=white@0.85,tpad=stop_mode=clone:stop_duration=1[b];\
[a][b]hstack=inputs=2" -c:v libx264 -crf 16 -pix_fmt yuv420p -movflags +faststart out/cp2_A_vs_B_side_by_side.mp4
# safe-zone overlay version of each final frame
for v in A B; do
  convert work/$v/f_0119.png \( -size 1080x1920 xc:none -fill "rgba(255,40,40,0.22)" -draw "rectangle 0,0 1079,219" -draw "rectangle 0,1500 1079,1919" -draw "rectangle 920,220 1079,1499" \) -composite -quality 88 out/cp2_${v}_end_safezone.jpg
done
# keyframe strips
for v in A B; do
  convert work/$v/f_0000.png work/$v/f_0030.png work/$v/f_0060.png work/$v/f_0090.png work/$v/f_0119.png -resize 324x576 +append out/cp2_${v}_keyframes.jpg
done
ls -la out
