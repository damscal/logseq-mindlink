// Import dotenv and configure it
import * as dotenv from 'dotenv';
dotenv.config();
// Access environment variables
const gemini_api_key = process.env.GOOGLE_API_KEY;

// importing classes
import {
    SimpleDirectoryReader,
    VectorStoreIndex,
    MarkdownReader,
    Gemini,
    GEMINI_MODEL,
    GeminiEmbedding,
    Settings,
} from "llamaindex";

// define a markdown parser with removeHyperlinks=false and removeImages= false
const parser = new MarkdownReader(false,false);

// load documents
const reader = new SimpleDirectoryReader();
const documents1 = await reader.loadData({
    directoryPath: "/logseq/journals",
    defaultReader: parser,
});
const documents2 = await reader.loadData({
    directoryPath: "/logseq/pages",
    defaultReader: parser,
});
const documents = documents1.concat(documents2);


Settings.embedModel = new GeminiEmbedding();
Settings.llm = new Gemini({
    model: GEMINI_MODEL.GEMINI_PRO,
  });

const index = await VectorStoreIndex.fromDocuments(documents);

const queryEngine = index.asQueryEngine();

const query = "cosa ho discusso con il geometra Lovecchio?";

const results = await queryEngine.query({
  query,
});

console.log(results);
