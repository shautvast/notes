GET /(id: u32) -> Json<Customer>:
    service.get(id)

struct Customer:
    id: u32,
    first_name: string,
    last_name: string
