#
# Master クラスのテスト
#
require 'test/unit'
require 'player'
require 'table'
require 'master'
require 'hand'
require 'card'

#
# テスト用 Player クラス
#
class PlayerMock < Player
		
  def initialize(name, master, table, hand)
    super(name, master, table, hand)
    @my_hand = hand
    @recorder = ""
  end
		
  # プレイの記録を残す
  def play(next_player)
    @recorder.concat(next_player.to_s + ":" + @my_hand.to_s)
    super(next_player)
    @recorder.concat("-> " + @my_hand.to_s)
  end
		
  def get_record
    return @recorder
  end

end

#
# テスト用 Hand クラス
#
class HandMock < Hand
  # shuffle しても持手が換わらないようにする
  def shuffle
  end
end


class TestMaster < Test::Unit::TestCase

  def setup
  end

  def teardown
  end

  def test_master
    table = Table.new
    master = Master.new
    # テスト用 Mock の作成
    hand1 = HandMock.new
    hand2 = HandMock.new
    hand3 = HandMock.new

    # プレイヤー作成&登録
    p1 = PlayerMock.new("P1", master, table, hand1)
    p2 = PlayerMock.new("P2", master, table, hand2)
    p3 = PlayerMock.new("P3", master, table, hand3)
    master.register_player(p1)
    master.register_player(p2)
    master.register_player(p3)
		
    # 最初のカードを作る
    hand0 = HandMock.new()
    hand0.add_card(Card.new(Card::SUIT_HEART, 2))
    hand0.add_card(Card.new(Card::SUIT_HEART, 2))
    hand0.add_card(Card.new(Card::SUIT_SPADE, 2))
    hand0.add_card(Card.new(Card::SUIT_SPADE, 3))
    hand0.add_card(Card.new(Card::SUIT_CLUB, 3))
    hand0.add_card(Card.new(Card::SUIT_CLUB, 3))
    hand0.add_card(Card.new(Card::SUIT_DIAMOND, 5))

    # カード準備のチェック
    master.prepare_game(hand0)
    assert_equal("H2 S3 D5 ", hand1.to_s)
    assert_equal("H2 C3 ", hand2.to_s)
    assert_equal("S2 C3 ", hand3.to_s)
		
    #ゲーム開始のチェック
    master.start_game()
    assert_equal("P2:H2 S3 D5 -> S3 D5 ", p1.get_record())
    assert_equal("P3:C3 -> C3 S2 P1:C3 S2 -> C3 S2 D5 ", p2.get_record())
    assert_equal("P1:C3 -> ", p3.get_record())
  end

end
