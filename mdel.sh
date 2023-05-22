# !/bin/bash
DLEETE_MEDIA=("mediafiles/reward_images" "mediafiles/profile_pics" "mediafiles/schools" "mediafiles/submissions")
  for app in "${DLEETE_MEDIA[@]}"; do
  find "$app/" -mindepth 1  -delete
  done