import csv
import datetime

now_time = datetime.datetime.utcnow()

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price


### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list = []
        self.item_num_list = []
        self.total_price = 0
        self.receipt = []
        self.item_master = item_master
    
    def add_item_order(self,item_code, num):
        self.item_order_list.append(item_code)
        self.item_num_list.append(num)
        
    def view_item_list(self):
        for code in self.item_order_list:
            for k in range(1, len(self.item_master)):
                if self.item_master[k][0] == code:
                    print("商品コード:{0}  商品名:{1}  価格:{2}".format(self.item_master[k][0], self.item_master[k][1], self.item_master[k][2]))
                    self.receipt.extend(f"商品コード:{self.item_master[k][0]}  商品名:{self.item_master[k][1]}  価格:{self.item_master[k][2]}\n")
                    print(f"{self.item_num_list[self.item_order_list.index(code)]}個")
                    self.receipt.extend(f"{self.item_num_list[self.item_order_list.index(code)]}個\n")
                    self.total_price += int(self.item_master[k][2]) * int(self.item_num_list[self.item_order_list.index(code)])
        print(f"合計金額は {self.total_price} 円です。")
        self.receipt.extend(f"\n合計金額: {self.total_price} 円\n")

    def cashier(self):
        pay = int(input("\nいくらお支払いされますか？ >>> "))
        self.receipt.extend(f"支払金額: {pay} 円\n")
        if pay < self.total_price:
            print("お金が足りません！")
        else:
            cal_result = pay - self.total_price
            print(f"{cal_result} 円のお釣りになります！  ありがとうございました！")
            self.receipt.extend(f"お釣り: {cal_result} 円\n")
            with open(f"receipt_{now_time}.txt", "w") as li:
                li.write(f"{now_time}\n\n")
                for e in self.receipt:
                    li.write(e)





    
### メイン処理

def main():

    with open("item_list.csv") as f:
        item_master = [row for row in csv.reader(f)]
    
    # オーダー登録
    order=Order(item_master)
    print("ようこそ！  購入したい商品が決まったら「ok」と入力してください！")
    while True:
        item = input("購入したい商品の商品コードを入力してください >>> ")
        if item == "ok":
            print("\n 下記の商品を購入しました！")
            break
        num = input("何個購入しますか？  （例: 1） >>> ")
        order.add_item_order(item, num)
    
    # オーダー表示
    order.view_item_list()
    # 会計
    order.cashier()

    
if __name__ == "__main__":
    main()