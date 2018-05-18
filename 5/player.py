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
  # 与えられた戦略
  # @tactics

  #------------------------
  # プレイヤークラスの操作
  #------------------------


  #
  # プレイヤークラスのコンストラクタ。
  #
  def initialize(name)
    @name = name
    @win_count = 0
    @tactics = nil
  end


  #
  # ジャンケンの手を出す。
  #
  def show_hand()
    # 与えられた戦略を読んでジャンケンの手を決める
    hand = @tactics.read_tactics()

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


  #
  # 戦略を設定
  #
  def set_tactics(tactics)
    @tactics = tactics
  end

  # set_tactics( は attr_writer :tactics で良い
end
