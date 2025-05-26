-- db schema depends on imported CSV and verified manually

DROP TABLE IF EXISTS markets;
DROP TABLE IF EXISTS reviews;

CREATE TABLE markets (
    -- Market data
    fmid TEXT PRIMARY KEY,
    market_name TEXT,
    street TEXT,
    city TEXT,
    county TEXT,
    state TEXT,
    zip TEXT,
    x REAL,
    y REAL,
    website TEXT,
    facebook TEXT,
    twitter TEXT,
    youtube TEXT,
    other_media TEXT,
    update_time TEXT,
    -- Payment options
    credit TEXT,
    wic TEXT,
    wiccash TEXT,
    sfmnp TEXT,
    snap TEXT,
    -- Product categories
    organic TEXT,
    bakedgoods TEXT,
    cheese TEXT,
    crafts TEXT,
    flowers TEXT,
    eggs TEXT,
    seafood TEXT,
    herbs TEXT,
    vegetables TEXT,
    honey TEXT,
    jams TEXT,
    maple TEXT,
    meat TEXT,
    nursery TEXT,
    nuts TEXT,
    plants TEXT,
    poultry TEXT,
    prepared TEXT,
    soap TEXT,
    trees TEXT,
    wine TEXT,
    coffee TEXT,
    beans TEXT,
    fruits TEXT,
    grains TEXT,
    juices TEXT,
    mushrooms TEXT,
    petfood TEXT,
    tofu TEXT,
    wildharvested TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    market_id TEXT,
    name TEXT,
    surname TEXT,
    rating INTEGER,
    review TEXT
);
