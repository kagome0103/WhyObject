#
#== ジャンケンのプレイヤーを表すクラス。
#
class Player
  # ジャンケンの手を表す定数
  STONE = 0 # グー
  SCISSORS = 1 # チョキ
  PAPER = 2 # パー

  #------------------------
  # プレイヤークラスの属性
  #------------------------

  # プレイヤーの名前 
  # @name
  # プレイヤーの勝った回数 
  # @win_count

  #------------------------
  # プレイヤークラスの操作
  #------------------------


  #
  # プレイヤークラスのコンストラクタ。
  #
  def initialize(name)
    @name = name
    @win_count = 0
  end


  #
  # ジャンケンの手を出す。
  #
  def show_hand()
    # プレイヤーの手
    hand = 0

    # 0.0以上3.0未満の小数として乱数を得る
    random_num = rand()* 3.0
    if (random_num < 1.0)
      # randomNum が 0.0以上1.0未満の場合、グー
      hand = STONE
    elsif (random_num < 2.0)
      # randomNum が 1.0以上2.0未満の場合、チョキ
      hand = SCISSORS
    elsif (random_num < 3.0)
      # randomNum が 2.0以上3.0未満の場合、パー
      hand = PAPER
    end

    # 決定した手を戻り値として返す
    return hand
  end

  #
  # 審判から勝敗を聞く。勝ったら、引数 result は true
  #
  def notify_result(result)
    if (result)
      # 勝った場合は勝ち数を加算する
      @win_count += 1
    end
  end

  #
  # 自分の勝った回数を答える。
  #
  def get_win_count()
    return @win_count
  end

  #
  # 自分の名前を答える。
  # 
  def get_name()
    return @name
  end

  # get_win_count(), get_name() は attr_reader :win_count :name で良い
end
