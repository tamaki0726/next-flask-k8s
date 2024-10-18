// 部品の詳細情報
export type Detail = {
    detailName: string;
    amount: number;
    count: number;
};

// コンテンツ全体の情報
export type Content = {
    contentsName: string;
    userName: string;
    createdAt: string;
    details: Detail[];
};
