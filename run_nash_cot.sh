# python nash_cot.py --method few_shot_cot \
#                    --dataset multiarith \
#                    --random_seed 15 \
#                    --sub_dir experiments \
#                    --tokenizer_path 3 \
#                    --model_tag 2 \
#                    --inner_loop 2 \
#                    --outer_loop 3

# python nash_cot.py --method zero_shot_cot \
#                    --dataset math-500 \
#                    --random_seed 15 \
#                    --sub_dir experiments \
#                    --tokenizer_path 3 \
#                    --model_tag 2 \
#                    --inner_loop 2 \
#                    --outer_loop 3

# python nash_cot.py --method zero_shot_cot \
#                    --dataset aime2024 \
#                    --random_seed 15 \
#                    --sub_dir experiments \
#                    --tokenizer_path 3 \
#                    --model_tag 2 \
#                    --inner_loop 2 \
#                    --outer_loop 3

# python nash_cot.py --method zero_shot_cot \
#                    --dataset amc2023 \
#                    --random_seed 15 \
#                    --sub_dir experiments \
#                    --tokenizer_path 3 \
#                    --model_tag 2 \
#                    --inner_loop 2 \
#                    --outer_loop 2

python nash_cot.py --method zero_shot_cot \
                   --dataset gaokao-mathqa \
                   --random_seed 15 \
                   --sub_dir experiments \
                   --tokenizer_path 3 \
                   --model_tag 2 \
                   --inner_loop 2 \
                   --outer_loop 2
