out_csv='results_output.csv'

python save_cocoEval.py --n_bit=32 --language='python' --output_csv_file=$out_csv --overwrite=True
python save_cocoEval.py --n_bit=32 --language='cpp' --output_csv_file=$out_csv --overwrite=False
python save_cocoEval.py --n_bit=64 --language='python' --output_csv_file=$out_csv --overwrite=False
python save_cocoEval.py --n_bit=64 --language='cpp' --output_csv_file=$out_csv --overwrite=False