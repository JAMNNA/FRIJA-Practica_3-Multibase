use("Practica_3")
//switched to db Practica_3
db.createCollection("brands", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["name", "country_of_origin", "status"],
         properties: {
            name: { bsonType: "string", maxLength: 60 },
            country_of_origin: { bsonType: "string", maxLength: 50 },
            status: { enum: ["ACTIVE", "INACTIVE"] }
         }
      }
   }
});

// Índice Único
db.brands.createIndex({ name: 1 }, { unique: true });
db.createCollection("categories", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["name", "status"],
         properties: {
            name: { bsonType: "string", maxLength: 40 },
            description: { bsonType: "string", maxLength: 150 },
            status: { enum: ["ACTIVE", "INACTIVE"] }
         }
      }
   }
});

// Índice Único
db.categories.createIndex({ name: 1 }, { unique: true });
db.createCollection("products", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["name", "brand_id", "category_id", "presentation", "content_ml", "alcohol_content", "sale_price", "status"],
         properties: {
            name: { bsonType: "string", maxLength: 100 },
            brand_id: { bsonType: "objectId", description: "Referencia a brands" },
            category_id: { bsonType: "objectId", description: "Referencia a categories" },
            presentation: { bsonType: "string", maxLength: 30 },
            content_ml: { bsonType: "int" },
            alcohol_content: { bsonType: "decimal" },
            sale_price: { bsonType: "decimal" },
            status: { enum: ["ACTIVE", "INACTIVE", "DISCONTINUED"] }
         }
      }
   }
});

// Índices
db.products.createIndex({ brand_id: 1 });
db.products.createIndex({ category_id: 1 });
db.products.createIndex({ status: 1 });
use("Practica_3");

// ============================================================
// 1.Brands
// ============================================================
db.brands.insertMany([
   { 
      _id: ObjectId("600000000000000000000001"), 
      name: "Heineken", 
      country_of_origin: "Netherlands", 
      status: "ACTIVE" 
   },
   { 
      _id: ObjectId("600000000000000000000002"), 
      name: "Corona", 
      country_of_origin: "Mexico", 
      status: "ACTIVE" 
   },
   { 
      _id: ObjectId("600000000000000000000003"), 
      name: "Guinness", 
      country_of_origin: "Ireland", 
      status: "ACTIVE" 
   }
]);

// ============================================================
// 2.Categories
// ============================================================
db.categories.insertMany([
   { 
      _id: ObjectId("700000000000000000000001"), 
      name: "Lager", 
      description: "Light and refreshing beer", 
      status: "ACTIVE" 
   },
   { 
      _id: ObjectId("700000000000000000000002"), 
      name: "Pilsner", 
      description: "Crisp and balanced beer", 
      status: "ACTIVE" 
   },
   { 
      _id: ObjectId("700000000000000000000003"), 
      name: "Stout", 
      description: "Dark and roasted beer", 
      status: "ACTIVE" 
   }
]);

// ============================================================
// 3. Products
// ============================================================
db.products.insertMany([
   {
      name: "Heineken Original",
      brand_id: ObjectId("600000000000000000000001"), // Heineken
      category_id: ObjectId("700000000000000000000001"), // Lager
      presentation: "Bottle",
      content_ml: NumberInt(355),
      alcohol_content: NumberDecimal("5.00"),
      sale_price: NumberDecimal("35.00"),
      status: "ACTIVE"
   },
   {
      name: "Heineken Silver",
      brand_id: ObjectId("600000000000000000000001"), // Heineken
      category_id: ObjectId("700000000000000000000002"), // Pilsner
      presentation: "Bottle",
      content_ml: NumberInt(355),
      alcohol_content: NumberDecimal("4.00"),
      sale_price: NumberDecimal("37.00"),
      status: "ACTIVE"
   },
   {
      name: "Corona Extra",
      brand_id: ObjectId("600000000000000000000002"), // Corona
      category_id: ObjectId("700000000000000000000001"), // Lager
      presentation: "Bottle",
      content_ml: NumberInt(355),
      alcohol_content: NumberDecimal("4.50"),
      sale_price: NumberDecimal("32.00"),
      status: "ACTIVE"
   },
   {
      name: "Corona Familiar",
      brand_id: ObjectId("600000000000000000000002"), // Corona
      category_id: ObjectId("700000000000000000000001"), // Lager
      presentation: "Bottle",
      content_ml: NumberInt(940),
      alcohol_content: NumberDecimal("4.50"),
      sale_price: NumberDecimal("55.00"),
      status: "ACTIVE"
   },
   {
      name: "Guinness Draught",
      brand_id: ObjectId("600000000000000000000003"), // Guinness
      category_id: ObjectId("700000000000000000000003"), // Stout
      presentation: "Can",
      content_ml: NumberInt(440),
      alcohol_content: NumberDecimal("4.20"),
      sale_price: NumberDecimal("55.00"),
      status: "ACTIVE"
   },
   {
      name: "Guinness Extra Stout",
      brand_id: ObjectId("600000000000000000000003"), // Guinness
      category_id: ObjectId("700000000000000000000003"), // Stout
      presentation: "Bottle",
      content_ml: NumberInt(330),
      alcohol_content: NumberDecimal("5.60"),
      sale_price: NumberDecimal("48.00"),
      status: "ACTIVE"
   }
]);

db.products.find()