from datetime import datetime

import boto3

def lambda_handler(event, context):
    
    ec2 = boto3.client('ec2')
    
    # grab regions
    regions = [region['RegionName']
        for region in ec2.describe_regions()['Regions']]
    
    # iterate through regions 
    for region in regions:
        print('Instances in EC2 Region {0}:'.format(region))
        
        
        ec2_resource = boto3.resource('ec2', region_name = region)
        
        # filter for tag 'backup' and value of 'true'
        instances = ec2_resource.instances.filter(
            Filters = [
                {'Name': 'tag:backup', 'Values': ['true']}
            ]
        )
        
        # ISO 8601 timestamp
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
        
        # iterate through instances 
        for i in instances.all():
            
            # iterate through volumes
            for v in i.volumes.all():
                
                # variable that holds the instance id, volume id and timestamp
                desc = 'Backup of {0}, volume {1}, created {2}'.format(
                    i.id, 
                    v.id,
                    timestamp)
                print(desc)
                
                # create the snapshot
                snapshot = v.create_snapshot(Description = desc)
                
                print('Created snapshot:', snapshot.id)
                
                