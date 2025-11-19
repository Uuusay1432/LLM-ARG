#!/bin/zsh

# エラーが発生した場合にスクリプトを停止し、エラーメッセージを表示
set -e

# 初期設定
BASE_DIR=$(dirname $(realpath $0)) # このスクリプトのあるディレクトリ
SWIM_DIR="$BASE_DIR/.."       # SWIMプロジェクトのルート
RESULT_DIR="$SWIM_DIR/results"     # 結果ディレクトリ

cd "$BASE_DIR"

make

cd "$BASE_DIR/simulations/swim_sa"

./run.sh My 7

cd "$RESULT_DIR"

../swim/tools/plotResults.sh SWIM_SA My 7 plot.pdf  && open plot.pdf
