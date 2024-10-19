export const kongGatewayEndpoint =
    process.env.KONG_GATEWAY_URL ?? ('http://localhost:8000' as string);
