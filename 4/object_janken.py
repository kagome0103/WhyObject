#
#== オブジェクト指向によるジャンケンプログラム
#
require 'murata'
require 'yamada'
require 'judge'


# 審判（斎藤さん）のインスタンス生成
saito = Judge.new

# プレイヤー１（村田さん）の生成
murata = Murata.new

# プレイヤー２（山田さん）の生成
yamada = Yamada.new

# 村田さんと山田さんをプレイヤーとしてジャンケンを開始する
saito.start_janken(murata, yamada)
