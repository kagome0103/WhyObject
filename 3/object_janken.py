#
#== オブジェクト指向によるジャンケンプログラム
#
require 'player'
require 'judge'


# 審判（斎藤さん）のインスタンス生成
saito = Judge.new

# プレイヤー１（村田さん）の生成
murata = Player.new("村田さん")

# プレイヤー２（山田さん）の生成
yamada = Player.new("山田さん")

# 村田さんと山田さんをプレイヤーとしてジャンケンを開始する
saito.start_janken(murata, yamada)
