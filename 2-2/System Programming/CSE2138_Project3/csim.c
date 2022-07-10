#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>
#include "cachelab.h"

typedef struct arguments {
    int h;
    int v;
    int s;
    int E;
    int b;
    char * t;
} Arguments;

typedef struct cache_line {
    int valid_bit;
    int tag_bit;
    int times;
} CacheLine;

typedef CacheLine * CacheSet;
typedef CacheSet * Cache;

void get_args(Arguments * args, int argc, char ** argv) {
    int opt;
    while(-1 != (opt = getopt(argc, argv, "hvs:E:b:t:"))) {
        switch(opt) {
        case 'h':
            args->h = 1;
            break;
        case 'v':
            args->v = 1;
            break;
        case 's':
            args->s = atoi(optarg);
            break;
        case 'E':
            args->E  = atoi(optarg);
            break;
        case 'b':
            args->b = atoi(optarg);
            break;
        case 't':
            args->t = (char*)malloc(sizeof(char) * strlen(optarg));
            strcpy(args->t, optarg);
            break;
        default:
            fprintf(stderr, "wrong argument\n");
            exit(0);
            break;
        }
    }
}

void process_help(Arguments args) {
    if(args.h == 1 || args.s == -1 ||
            args.E  == -1 || args.b == -1 ||
            args.t == NULL) {
        FILE * fp = fopen("help.txt", "rt");
        char c;
        while(fscanf(fp, "%c", &c) != EOF) {
            putchar(c);
        }
        fclose(fp);
        exit(0);
    }
}

int hit_count = 0;
int miss_count = 0;
int eviction_count = 0;

void init_args(Arguments * args) {
    args->h = 0;
    args->v = 0;
    args->s = -1;
    args->E = -1;
    args->b = -1;
    args->t = NULL;
}

void init_cache(Cache * cache, Arguments * args) {
    int set_size = 1 << args->s;
    int num_lines = args->E;
    *cache = (CacheSet *)malloc(sizeof(CacheSet) * set_size);
    for(int i =0; i<set_size; ++i) {
        (*cache)[i] = (CacheLine*)malloc(sizeof(CacheLine)*num_lines);
        for(int j = 0; j<num_lines; ++j) {
            (*cache)[i][j].valid_bit = 0;
            (*cache)[i][j].tag_bit = -1;
            (*cache)[i][j].times = 0;
        }
    }
}

void process(Cache * cache, Arguments * args, int address) {
    address >>= args->b;
    int set_index = 0;
    int tag_bits, i;
    long mask = 0xffffffffffffffff >> (64 - args->s);
    set_index = mask & address;
    address >>= args->s;
    tag_bits = address;
    CacheSet set = (*cache)[set_index];
    for (i = 0; i < args->E; ++i) {
        if (set[i].valid_bit == 1) {
            set[i].times++;
        }
    }
    for (i = 0; i < args->E; ++i) {
        if (set[i].valid_bit == 1 && set[i].tag_bit == tag_bits) {
            if(args->v) printf(" hit");
            set[i].times = 0;
            ++hit_count;
            return;
        }
    }

    ++miss_count;
    if(args->v) printf(" miss");
    for (i = 0; i < args->E; ++i) {
        if (set[i].valid_bit == 0) {
            set[i].tag_bit = tag_bits;
            set[i].valid_bit = 1;
            set[i].times = 0;
            return;
        }
    }

    ++eviction_count;
    if(args->v) printf(" eviction");
    int max_index = 0, max_time = set[0].times;
    for (i = 0; i < args->E; ++i) {
        if (set[i].times > max_time) {
            max_index = i;
            max_time = set[i].times;
        }
    }
    set[max_index].tag_bit = tag_bits;
    set[max_index].times = 0;
}
int main(int argc, char ** argv) {
    Arguments args;
    init_args(&args);
    get_args(&args, argc, argv);
    process_help(args);

    Cache cache;
    init_cache(&cache, &args);

    FILE * fp = fopen(args.t, "r");
    if(fp == NULL) {
        printf("%s: No such file or directory\n", args.t);
        exit(1);
    }
    char op;
    unsigned address;
    int size = -1;
    while(fscanf(fp, " %c %x,%d", &op, &address, &size) > 0) {
        if(size==-1) continue;
        switch(op) {
        case 'I':
            break;
        case 'M':
            if(args.v) printf("M, %x, %d", address, size);
            process(&cache, &args, address);
            process(&cache, &args, address);
            if(args.v) printf("\n");
            break;
        case 'L':
            if(args.v) printf("L, %x, %d", address, size);
            process(&cache, &args, address);
            if(args.v) printf("\n");
            break;
        case 'S':
            if(args.v) printf("S, %x, %d", address, size);
            process(&cache, &args, address);
            if(args.v) printf("\n");
            break;
        default:
            printf("Error: invalid operation.");
            exit(0);
        }
    }
    fclose(fp);
    printSummary(hit_count, miss_count, eviction_count);
    for(int i = 0; i<(1<<args.s); ++i) {
        free(cache[i]);
    }
    free(cache);
    return 0;
}