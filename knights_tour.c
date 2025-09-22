#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define SIZE 8
#define MAX_ROUTE 64

typedef struct {
    int y;
    int x;
} Pos;

void init_chess(char board[SIZE][SIZE]);
void print_chess(const char board[SIZE][SIZE]);
Pos knight_present_position(const char board[SIZE][SIZE]);
int knight_next_positions(const char board[SIZE][SIZE], Pos present, Pos next_list[8]);
void move_knight(char board[SIZE][SIZE], Pos present, Pos next_list[8], int n_next);
void route_recorder(Pos route[], int *len, Pos present);
bool check_success(const char board[SIZE][SIZE]);
bool knights_tour(void);

int main(void) {
    srand((unsigned)time(NULL));
    for (int i = 0; i < 10000000; i++) {
        printf("Attempt %d\n", i);
        bool result = knights_tour();
        if (result) break;
    }
    return 0;
}

void init_chess(char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int k = 0; k < SIZE; k++) {
            if (i == 7 && k == 0) board[i][k] = 'N';   
            else board[i][k] = 'O';                    
        }
    }
}

void print_chess(const char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int k = 0; k < SIZE; k++) {
            printf("%c ", board[i][k]);
        }
        printf("\n");
    }
}

Pos knight_present_position(const char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int k = 0; k < SIZE; k++) {
            if (board[i][k] == 'N') {
                Pos p = { i, k };
                return p;
            }
        }
    }
    Pos none = { -1, -1 };
    return none;
}

int knight_next_positions(const char board[SIZE][SIZE], Pos present, Pos next_list[8]) {
    int dy[8] = {  2,  2, -2, -2,  1,  1, -1, -1 };
    int dx[8] = {  1, -1,  1, -1,  2, -2,  2, -2 };
    int count = 0;

    for (int i = 0; i < 8; i++) {
        int ny = present.y + dy[i];
        int nx = present.x + dx[i];
        if (ny >= 0 && ny < SIZE && nx >= 0 && nx < SIZE) {
            if (board[ny][nx] == 'O') {
                next_list[count].y = ny;
                next_list[count].x = nx;
                count++;
            }
        }
    }
    return count;
}

void move_knight(char board[SIZE][SIZE], Pos present, Pos next_list[8], int n_next) {
    if (n_next <= 0) return;
    int idx = rand() % n_next;
    Pos where = next_list[idx];

    board[present.y][present.x] = 'X';
    board[where.y][where.x] = 'N';
}

void route_recorder(Pos route[], int *len, Pos present) {
    if (*len < MAX_ROUTE) {
        route[*len] = present;
        (*len)++;
    }
}

bool check_success(const char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int k = 0; k < SIZE; k++) {
            if (board[i][k] == 'O') return false;
        }
    }
    return true;
}

bool knights_tour(void) {
    char board[SIZE][SIZE];
    Pos route[MAX_ROUTE];
    int route_len = 0;

    init_chess(board);

    Pos present = knight_present_position(board);
    route_recorder(route, &route_len, present);

    Pos next_list[8];
    int n_next = knight_next_positions(board, present, next_list);
    move_knight(board, present, next_list, n_next);

    while (1) {
        present = knight_present_position(board);
        route_recorder(route, &route_len, present);

        n_next = knight_next_positions(board, present, next_list);
        if (n_next == 0) break;

        move_knight(board, present, next_list, n_next);
    }

    printf("Route Length: %d\n", route_len);

    if (check_success(board)) {
        printf("Knight's Tour Success.\n\n");
        print_chess(board);

        printf("Route (y, x):\n");
        for (int i = 0; i < route_len; i++) {
            printf("(%d, %d)", route[i].y, route[i].x);
            if (i < route_len - 1) printf(" -> ");
        }
        printf("\n\n");

        return true;
    } else {
        printf("Knight's Tour Fail.\n\n");
        return false;
    }
}