#include <iostream>
#include <map>
#include <string>
#include <math.h>
using namespace std;

int main ()
{
  int n;
  char name[32];
  string round_names[1001];
  int round_scores[1001];
  int points, new_points;

  scanf("%d", &n);

  map<string, int> scores;

  for (int i = 0; i < n; i++) {
    scanf("%s %d", name, &points);
    round_names[i] = name;
    scores[name] += points;
    round_scores[i] = scores[name];
  }

  int m = -1;
  for (int i = 0; i < n; i++) {
    m = max(m, scores[round_names[i]]);
  }

  for (int i = 0; i < n; i++) {
    if (round_scores[i] >= m && scores[round_names[i]] == m) {
      cout << round_names[i] << "\n";
      break;
    }
  }

  return 0;
}

