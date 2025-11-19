CXX = g++  # 使用するC++コンパイラ
CXXFLAGS = -O3 -Wall -fmessage-length=0 -std=c++17  # C++17を指定
LDFLAGS = -L/usr/local/lib  # 必要に応じてBoostのライブラリパスを指定
LIBS = -lboost_system -lpthread

# ソースファイルとオブジェクトファイル
OBJS = simple_am.o SwimClient.o
TARGET = simple_am

TEST = $(TARGET)_test
TEST_OBJS = SwimClient.o SwimClientTest.o

# ターゲットのビルドルール
$(TARGET): $(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) $(LIBS)

all: $(TARGET)

# テストターゲットのビルドルール
test: $(TEST)
	./$(TEST)

$(TEST): $(TEST_OBJS)
	$(CXX) -o $(TEST) $(TEST_OBJS) $(LIBS)

# オブジェクトファイルの削除
clean:
	rm -f $(OBJS) $(TEST_OBJS) $(TARGET) $(TEST)
