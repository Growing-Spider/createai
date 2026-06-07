This directory stores the U-Net pre-trained model weights file.

Expected file: unet_model.pth

Obtaining the model weights:
-------------------------------
Option 1 (Recommended): Train on DRIVE Dataset
  - Download DRIVE dataset: https://drive.grand-challenge.org/
  - Run: python train_unet.py --dataset DRIVE --epochs 50
  - The trained weights will be saved here automatically.

Option 2: Use STARE or CHASEDB1 dataset
  - Both are publicly available retinal vessel segmentation datasets.

Option 3: Demo Mode (No weights needed)
  - If this file does not exist, the platform will automatically
    use Frangi filter-based vessel segmentation for demonstration.
  - Performance is reduced but the platform remains fully functional.

Model Architecture:
-------------------------------
- U-Net (Ronneberger et al., MICCAI 2015)
- Input: 512×512 RGB fundus image
- Output: 512×512 binary vessel mask
- Parameters: ~31M

Reference:
-------------------------------
Ronneberger, O., Fischer, P., & Brox, T. (2015).
U-net: Convolutional networks for biomedical image segmentation.
MICCAI 2015, 234-241.
