## Initial Testing

### Command
`python main_test_vrt.py --task 001_VRT_videosr_bi_REDS_6frames --folder_lq testsets/REDS4/sharp_bicubic --folder_gt testsets/REDS4/GT --tile 20 128 128 --tile_overlap 2 20 20`

### Results
```
Testing 000  (0/4) - PSNR: 28.40 dB; SSIM: 0.8383; PSNR_Y: 29.73 dB; SSIM_Y: 0.8499
Testing 011  (1/4) - PSNR: 32.69 dB; SSIM: 0.8934; PSNR_Y: 34.00 dB; SSIM_Y: 0.9000
Testing 015  (2/4) - PSNR: 34.68 dB; SSIM: 0.9257; PSNR_Y: 36.10 dB; SSIM_Y: 0.9338
Testing 020  (3/4) - PSNR: 30.52 dB; SSIM: 0.8958; PSNR_Y: 31.88 dB; SSIM_Y: 0.9079

results/001_VRT_videosr_bi_REDS6_6frames
-- Average PSNR: 31.57 dB; SSIM: 0.8833; PSNR_Y: 32.95 dB; SSIM_Y: 0.9014
```

### Command
`python main_test_vrt.py --task 002_VRT_videosr_bi_REDS_16frames --folder_lq testsets/REDS4/sharp_bicubic --folder_gt testsets/REDS4/GT --tile 20 128 128 --tile_overlap 2 20 20 --save_result`

### Results
```
Testing 000                  ( 0/4) - PSNR: 28.78 dB; SSIM: 0.8526; PSNR_Y: 30.11 dB; SSIM_Y: 0.8632
Testing 011                  ( 1/4) - PSNR: 33.39 dB; SSIM: 0.9049; PSNR_Y: 34.80 dB; SSIM_Y: 0.9192
Testing 015                  ( 2/4) - PSNR: 35.19 dB; SSIM: 0.9318; PSNR_Y: 36.62 dB; SSIM_Y: 0.9442
Testing 020                  ( 3/4) - PSNR: 31.07 dB; SSIM: 0.9065; PSNR_Y: 32.44 dB; SSIM_Y: 0.9178

results/002_VRT_videosr_bi_REDS_16frames
-- Average PSNR: 32.11 dB; SSIM: 0.8989; PSNR_Y: 33.49 dB; SSIM_Y: 0.9111
```

Saved in `results\002_VRT_videosr_bi_REDS_16frames`

### Command
`python main_test_vrt.py --task 003_VRT_videosr_bi_Vimeo_7frames --folder_lq testsets/Vid4/BIx4 --folder_gt testsets/Vid4/GT --tile 16 128 128 --tile_overlap 2 20 20 --num_workers 4 --save_result`

### Results
```
Testing calendar             ( 0/4) - PSNR: 22.78 dB; SSIM: 0.8003; PSNR_Y: 24.55 dB; SSIM_Y: 0.8291
Testing city                 ( 1/4) - PSNR: 26.91 dB; SSIM: 0.8124; PSNR_Y: 28.46 dB; SSIM_Y: 0.8298
Testing foliage              ( 2/4) - PSNR: 25.30 dB; SSIM: 0.7659; PSNR_Y: 26.71 dB; SSIM_Y: 0.7793
Testing walk                 ( 3/4) - PSNR: 30.35 dB; SSIM: 0.9137; PSNR_Y: 31.76 dB; SSIM_Y: 0.9244

results/003_VRT_videosr_bi_Vimeo_7frames
-- Average PSNR: 26.34 dB; SSIM: 0.8231; PSNR_Y: 27.87 dB; SSIM_Y: 0.8407
```

Saved in `results\003_VRT_videosr_bi_Vimeo_7frames`

### Command

`python main_test_vrt.py --task 004_VRT_videosr_bd_Vimeo_7frames --folder_lq testsets/Vid4/BDx4 --folder_gt testsets/Vid4/GT --tile 16 128 128 --tile_overlap 2 20 20 --num_workers 4 --save_result`