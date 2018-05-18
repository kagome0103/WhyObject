#
# ばば抜きプログラム。
#
require 'player'
require 'table'
require 'master'
require 'card'

#
# 53枚のトランプを生成する。
# 
def create_trump
  trump = Hand.new
        
  # 各スート13枚のカードを生成する
  for number in 1..13
    trump.add_card(Card::new(Card::SUIT_CLUB, number))
    trump.add_card(Card::new(Card::SUIT_DIAMOND, number))
    trump.add_card(Card::new(Card::SUIT_HEART, number))
    trump.add_card(Card::new(Card::SUIT_SPADE, number))
  end
  # ジョーカーの作成
  trump.add_card(Card::new(0, Card::JOKER))

  return trump
end



# 進行役の生成
master = Master.new
# 場の生成
field = Table.new
# プレイヤーの生成
murata = Player.new("村田", master, field)
yamada = Player.new("山田", master, field)
saito  = Player.new("斎藤", master, field)
        
# 進行役へプレイヤーを登録
master.register_player(murata)
master.register_player(yamada)
master.register_player(saito)
        
# トランプを生成する
trump = create_trump()
        
# ゲームの準備をする
master.prepare_game(trump)
        
# ゲームを開始する
master.start_game()


# end     
