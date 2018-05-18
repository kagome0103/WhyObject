#
# Hand クラスのテスト
#
require 'test/unit'
require 'hand'
require 'card'

class TestHand < Test::Unit::TestCase

  def setup
    @h = Hand.new
    @h.add_card(Card.new(Card::SUIT_SPADE, 3))
    @h.add_card(Card.new(Card::SUIT_DIAMOND, 1))
    @h.add_card(Card.new(Card::SUIT_HEART, 11))
    @h.add_card(Card.new(Card::JOKER, 0))
  end

  def teardown
  end

  def test_make
    assert_equal(4, @h.get_number_of_cards)
    assert_equal("S3 DA HJ JK ", @h.to_s)
  end

  def test_shuffle
    org = @h.to_s
    @h.shuffle
    #puts org, @h
    assert_not_equal(org, @h.to_s)
  end
    
  def test_find_same_number_card
    assert_nil(@h.find_same_number_card)
    @h.add_card(Card.new(Card::SUIT_CLUB, 1))

    same = @h.find_same_number_card
    assert_equal("CA", same[0].to_s)
    assert_equal("DA", same[1].to_s)
  end

end
