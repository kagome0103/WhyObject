#
# ばば抜きの進行役を表すクラス。
#
require 'table'
require 'master'
require 'hand'
require 'card'

class Master
  # プレイヤーのリスト
  # @players

  #
  # コンストラクタ。
  # 
  def initialize()
    @players = []
  end

  #
  # ゲームの準備をする。
  # 
  def prepare_game(cards)
    print "【カードを配ります】\n"

    # トランプをシャッフルする
    cards.shuffle

    # トランプの枚数を取得する
    number_of_cards = cards.get_number_of_cards

    # プレイヤーの人数を取得する
    number_of_players = @players.size

    for index in 0..number_of_cards - 1
      # カードから一枚引く
      card = cards.pick_card

      # 各プレイヤーに順番にカードを配る
      player = @players[index % number_of_players]
      player.receive_card(card)
    end
  end

  #
  # ゲームを開始する。
  #
  def start_game
    print "\n【ばば抜きを開始します】\n"
    
    # プレイヤーの人数を取得する
    count = 0
    while (@players.size > 1) 
      player_index = count % @players.size
      next_player_index = (count + 1) % @players.size
      
      # 指名するプレイヤーの取得
      player = @players[player_index]
      # 次のプレイヤーの取得
      next_player = @players[next_player_index]
      
      # プレイヤーを指名する
      print "\n", player, "さんの番です", "\n"
      player.play(next_player)
      count += 1
    end
    
    # プレイヤーが上がって残り1名になるとループを抜ける
    print "【ばば抜きを終了しました】\n"
  end

  #
  # 上がりを宣言する。
  # 
  def declare_win(winner)
    # 上がったプレイヤー
    print winner, "さんが上がりました！\n"
    
    # 上がったプレイヤーをリストからはずす
    @players.delete(winner)
    
    # 残りプレイヤーが１人になった時は敗者を表示する
    if (@players.size == 1)
      loser = @players[0]
      print loser, "さんの負けです！\n"
    end
  end
  
  #
  # ゲームに参加するプレイヤーを登録する。
  # 
  def register_player(player)
    # リストに参加者を追加する
    @players << player
  end

end
