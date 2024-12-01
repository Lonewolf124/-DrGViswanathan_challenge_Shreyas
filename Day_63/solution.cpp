  int myAtoi(char *s) {
       int sg = 1, i = 0, r = 0;
        while (s[i] == ' ') {
            i++;
        }
        if (s[i] == '-' || s[i] == '+') {
            if (s[i] == '-') {
                sg = -1;
            }
            i++;
        }
        while (s[i] >= '0' && s[i] <= '9') {
            if (r > INT_MAX / 10 || (r == INT_MAX / 10 && s[i] - '0' > 7)) {
                if (sg == 1) {
                    return INT_MAX;
                } else {
                    return INT_MIN;
                }
            }
            r = 10 * r + (s[i] - '0');
            i++;
        }
        return r * sg;
    }
