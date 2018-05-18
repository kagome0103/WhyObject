#
# 戦略インターフェースに対応したジャンケンプログラム。
#
require 'player'
require 'judge'
require 'stone_only_tactics'
require 'random_tactics'

# 審判（斎藤さん）のインスタンス生成
saito = Judge.new

# プレイヤー１（村田さん）の生成
murata = Player.new("村田さん")
# 村田さんに渡す戦略クラスを生成する
murata_tactics = StoneOnlyTactics.new
murata.set_tactics(murata_tactics)

# プレイヤー２（山田さん）の生成
yamada = Player.new("山田さん")
yamada_tactics = RandomTactics.new
yamada.set_tactics(yamada_tactics)

# 村田さんと山田さんをプレイヤーとしてジャンケンを開始する
saito.start_janken(murata, yamada)
