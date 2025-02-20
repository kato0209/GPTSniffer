
        client = self.get_conn()
        self.log.info('Deleting ReferenceImage')
        name = ProductSearchClient.reference_image_path(
            project=project_id, location=location, product=product_id, reference_image=reference_image_id
        )
        response = client.delete_reference_image(name=name, retry=retry, timeout=timeout, metadata=metadata)
        self.log.info('ReferenceImage with the name [%s] deleted.', name)

        return MessageToDict(response)