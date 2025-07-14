import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js"
import { z } from 'zod'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'

const server = new McpServer({
    name: "My Server",
    version: "1.0.0"
})

server.tool("add", { a: z.number(), b: z.number() }, async function({a, b}){
    const sum = a + b
    return { content: [{ type: 'text', text: String(sum) }]}
})

const transport = new StdioServerTransport()
await server.connect(transport)
console.log("Server is ready")